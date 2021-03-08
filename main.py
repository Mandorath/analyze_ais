#!/bin/python
"""Main script."""
import fun_logger
import ruamel.yaml
import pandas as pd
import multiprocessing
import numpy as np
from extract import PreProcess
from command_line import parseOptions
from pro_yml import yaml_extract
from f_analyze import search_ais_gaps
# from search_ais_gaps import search_ais_gaps

log = fun_logger.init_log()
yml_tst = ruamel.yaml
df_ships = pd.DataFrame()
df_ship_type = pd.DataFrame()


def parallelize_dataframe(df, func, n_cores=8):
    df_split = np.array_split(df, n_cores)

    pool = multiprocessing.Pool(n_cores)
    df = pd.concat(pool.map(func, df_split))

    pool.close()
    pool.join()

    return df


def extract_classes(extract, df):
    print(yml_tst.safe_dump(extract))
    elem = extract['elem']
    column = extract['column']
    out_file = extract['out_file']
    rem_df = extract['remove_in_df']
    df_base = prepros.extract_rows_type(df, elem, column)
    prepros.csv_out(df_base, out_file)
    if rem_df:
        df = prepros.remove_rows(df, elem, column)


def extract_vessel_types(extract, df, df_ships):
    """
    Extracts the vessel types specified in the yaml file.

    Args:
       extract (dict): Yaml file, that contains instructions.
       df (df): Dataframe containing the data to extract parts of.
       df_ships: Dataframe that the extracted data will be put in.

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
        log.info("Extracting all rows matching MMSI {0}".format(uni_val))
        df_ship_type = prepros.extract_rows_type(df, uni_val, unique_col)
        print(df_ship_type)
        log.info("Adding vessel with MMSI {0} dataframe to vessel_type dataframe".format(uni_val))
        df_ships = pd.concat([df_ships, df_ship_type], ignore_index=True)
        # df = prepros.remove_rows(df, uni_val, unique_col)
        # prepros.csv_out(df, "remaining.out")
    prepros.csv_out(df_ships, out_file)


def analyze_vessels(extract, df, df_ships):
    elem = extract['elem']
    column = extract['column']
    out_file = extract['out_file']
    rem_df = extract['remove_in_df']
    unique_col = extract['unique_column']
    log.info("Extracting unique values from the column {0}".format(unique_col))
    l_unique = prepros.extract_uniq_val(df, unique_col)
    time = 6
    for uni_val in l_unique:
        df_ship_type = prepros.extract_rows_type(df, uni_val, unique_col)
        minutes = search_ais_gaps(df_ship_type, time)
        print(minutes)

if __name__ == '__main__':
    """Primary function."""
    parse_options = parseOptions()
    options = parse_options.arguments()
    prepros = PreProcess()
    yml = yaml_extract()
    # Configure logging
    fun_logger.handle_log(log, options.LOG)
    fun_logger.handle_console(log)
    # Parse argument options
    csv_file = options.CSV
    out_file = options.OUTPUT
    yml_file = options.YAML
    # load instructions
    instruct = yml.read_file(yml_file)
    print(yml_tst.safe_dump(instruct))
    # load CSV file
    df = prepros.csv_to_df(csv_file)
    # For all in extract block extract data.
    processes = []
    if 'extract' in instruct:
        for extract in instruct['extract']:
            p = multiprocessing.Process(target=extract_classes,
                                        args=(extract, df,))
            processes.append(p)
            p.start()
    if 'extract_vessel_types' in instruct:
        for extract in instruct['extract_vessel_types']:
            p = multiprocessing.Process(target=extract_vessel_types,
                                        args=(extract, df, df_ships,))
            p.start()
    if 'analyze' in instruct:
        for extract in instruct['analyze']:
            p = multiprocessing.Process(target=analyze_vessels,
                                        args=(extract, df, df_ships,))
            p.start()


            # prepros.csv_out(df_unique, out_file)
        # if rem_df:
        #    df = prepros.remove_rows(df, elem, column)
    # uniq = prepros.extract_uniq_val(df, 'MMSI')
    # search_mmsi(df, 'MMSI', uniq)


    # csv = file_h.read_csv(csv_file)
