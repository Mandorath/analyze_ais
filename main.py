#!/bin/python
"""Main script."""
import fun_logger
import ruamel.yaml
import os
import pandas as pd
import multiprocessing
import numpy as np
from extract import PreProcess
from command_line import parseOptions
from pro_yml import yaml_extract
from f_analyze import AnalyzeDf
from datetime import datetime

# from search_ais_gaps import search_ais_gaps

log = fun_logger.init_log()
yml_tst = ruamel.yaml
df_ships = []
df_ship_type = pd.DataFrame()


def return_data(data):
    df_ships.extend(data)

def parallelize_dataframe(func, args, n_cores=16):
    # df_split = np.array_split(df, n_cores)

    pool = multiprocessing.Pool(n_cores)
    df = pool.apply_async(func, args, callback=return_data)
    # df = pd.concat(pool.map(func, df_split))

    pool.close()
    pool.join()

    return df


def extract_classes(extract, df, out_dir):
    """
    Extracts the classes specified in the yaml file.

    Args:
    ----
       extract (dict): Yaml file, that contains instructions.
       df (df): Dataframe containing the data to extract parts of.

    """
    print(yml_tst.safe_dump(extract))
    elem = extract['elem']
    column = extract['column']
    out_file = extract['out_file']
    rem_df = extract['remove_in_df']
    df_base = prepros.extract_rows_type(df, elem, column)
    out_loc = "{0}/{1}".format(out_dir, out_file)
    prepros.csv_out(df_base, out_loc)
    if rem_df:
        df = prepros.remove_rows(df, elem, column)


def extract_vessel_types(df, uni_val, unique_col):
    log.info("Extracting all rows matching MMSI {0}".format(uni_val))
    df_ship_type = prepros.extract_rows_type(df, uni_val, unique_col)
    print(df_ship_type)
    log.info("Adding vessel with MMSI {0} dataframe to vessel_type dataframe".format(uni_val))
    df_ships.append(df_ship_type)
    # df_ships = pd.concat([df_ships, df_ship_type], ignore_index=True)


def prep_vessel_types(extract, df):
    """
    Extracts the vessel types specified in the yaml file.

    Args:
       extract (dict): Yaml file, that contains instructions.
       df (df): Dataframe containing the data to extract parts of.
       df_ships (df): Dataframe that the extracted data will be put in.

    """
    print(yml_tst.safe_dump(extract))
    elem = extract['elem']
    column = extract['column']
    out_file = extract['out_file']
    rem_df = extract['remove_in_df']
    unique_col = extract['unique_column']
    log.info("Extracting rows containing a ship type based on vessel type {0}".format(elem))
    df_base = prepros.extract_rows_type(df, elem, column)
    log.info("Extracting unique values from the column {0}".format(unique_col))
    l_unique = prepros.extract_uniq_val(df_base, unique_col)
    jobs = []
    for uni_val in l_unique:
        p = multiprocessing.Process(target=analysing_vessels,
                                    args=(df,
                                          uni_val,
                                          unique_col
                                          ))
        p.start()
    df_tot = pd.concat(df_ships)
    prepros.csv_out(df_tot, out_file)

def analysing_vessels(ais_gap, l_win, u_win, w_size, s_column, t_column, df,
                      l_poly, uni_val, unique_col):
    log.info("Extracting unique values.")
    df_ship_type = prepros.extract_rows_type(df, uni_val, unique_col)
    log.info("Searching for gaps in column {0}, based on {1}".format(t_column, ais_gap))
    df_ship_type = analyze.search_ais_gaps(df_ship_type, t_column, ais_gap)
    log.info("Calculating gradual change using column {0} and row size {1}".format(s_column, w_size))
    df_ship_type = analyze.grad_change(df_ship_type, s_column, w_size)
    df_ship_type = analyze.perc_change_incr(df_ship_type,
                                            'gr_prct',
                                            l_win,
                                            u_win)
    df_ship_type = analyze.perc_change_decr(df_ship_type,
                                            'gr_prct',
                                            l_win,
                                            u_win)
    geo_df = analyze.check_in_polygon(df_ship_type, l_poly)
    g_df = pd.DataFrame(geo_df)
    if not g_df.empty():
        g_df['Zn_entry'] = True
    # df_ships = pd.concat([df_ships, df_ship_type], ignore_index=True)
    # df_ships.append(df_ship_type)
    return df_ship_type, g_df


def prep_analysis(extract, df, l_poly, out_dir):
    out_file = extract['out_file']
    rem_df = extract['remove_in_df']
    unique_col = extract['unique_column']
    ais_gap = extract['ais_gap']
    l_win = extract['l_bound_win']
    u_win = extract['u_bound_win']
    w_size = extract['window_size']
    s_column = extract['speed_column']
    t_column = extract['time_column']
    log.info("Extracting unique values from the column {0}".format(unique_col))
    l_unique = prepros.extract_uniq_val(df, unique_col)
    results = []
    geo_results = []
    # n_cores = 30
    # pool = multiprocessing.Pool(n_cores)
    for uni_val in l_unique:
        df_shp, g_df = analysing_vessels(ais_gap, l_win, u_win, w_size,
                                         s_column, t_column, df, l_poly,
                                         uni_val, unique_col)
        # r = pool.apply_async(analysing_vessels, args, callback=return_data)
        results.append(df_shp)
        geo_results.append(g_df)
        # r = parallelize_dataframe(analysing_vessels, args)
    # pool.close()
    # pool.join()
    df_tot = pd.concat(results)
    df_t_g = pd.concat(geo_results)
    out_file2 = "geo_out"
    out_loc = "{0}/{1}".format(out_dir, out_file)
    out_loc = "{0}/{1}".format(out_dir, out_file2)
    prepros.csv_out(df_tot, out_loc)
    prepros.csv_out(df_t_g, out_loc)


def setup_dir(path):
    try:
        os.mkdir(path)
    except OSError:
        log.error("Creation of the directory %s failed" % path)
    else:
        log.info("Successfully created the directory %s " % path)


if __name__ == '__main__':
    """Primary function."""
    parse_options = parseOptions()
    options = parse_options.arguments()
    prepros = PreProcess()
    analyze = AnalyzeDf()
    yml = yaml_extract()
    # Configure logging
    fun_logger.handle_log(log, options.LOG)
    fun_logger.handle_console(log)
    # Parse argument options
    csv_file = options.CSV
    out_dir = options.OUTPUT
    yml_file = options.YAML
    # Create directory specified on CLI
    setup_dir(out_dir)
    # load instructions
    instruct = yml.read_file(yml_file)
    print(yml_tst.safe_dump(instruct))
    # load CSV file
    df = prepros.csv_to_df(csv_file)
    # For all in extract block extract data.
    processes = []
    if 'drop_columns' in instruct:
        l_columns = instruct['drop_columns']
        print(l_columns)
        df = prepros.drop_col(df, l_columns)
    if 'drop_columns' in instruct:
        l_poly = instruct['polygon']['poly_file']
        print(l_poly)
    if 'extract' in instruct:
        extr_class_Time = datetime.now()
        for extract in instruct['extract']:
            p = multiprocessing.Process(target=extract_classes,
                                        args=(extract, df, out_dir,))
            processes.append(p)
            p.start()
        total = datetime.now() - extr_class_Time
        print("Total time extracting vessels is: {0}".format(total))
    if 'extract_vessel_types' in instruct:
        extr_ves_Time = datetime.now()
        for extract in instruct['extract_vessel_types']:
            p = multiprocessing.Process(target=prep_vessel_types,
                                        args=(extract, df, out_dir,))
            p.start()
        total = datetime.now() - extr_ves_Time
        print("Total time extracting vessels is: {0}".format(total))
    if 'analyze' in instruct:
        analyzeTime = datetime.now()
        for extract in instruct['analyze']:
            p = multiprocessing.Process(target=prep_analysis,
                                        args=(extract,
                                              df,
                                              l_poly,
                                              out_dir,
                                              ))
            p.start()
        total = datetime.now() - analyzeTime
        print("Total time analysis is: {0}".format(total))


            # prepros.csv_out(df_unique, out_file)
        # if rem_df:
        #    df = prepros.remove_rows(df, elem, column)
    # uniq = prepros.extract_uniq_val(df, 'MMSI')
    # search_mmsi(df, 'MMSI', uniq)


    # csv = file_h.read_csv(csv_file)
