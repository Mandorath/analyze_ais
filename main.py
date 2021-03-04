#!/bin/python
"""Main script."""
import fun_logger
import ruamel.yaml
import pandas as pd
import multiprocessing
from extract import PreProcess
from command_line import parseOptions
from pro_yml import yaml_extract
# from search_ais_gaps import search_ais_gaps

log = fun_logger.init_log()
yml_tst = ruamel.yaml
df_ships = pd.DataFrame()


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
    print(yml_tst.safe_dump(extract))
    elem = extract['elem']
    column = extract['column']
    out_file = extract['out_file']
    rem_df = extract['remove_in_df']
    unique_col = extract['unique_column']
    df_base = prepros.extract_rows_type(df, elem, column)
    l_unique = prepros.extract_uniq_val(df_base, unique_col)

    for uni_val in l_unique:
        ret_value = multiprocessing.Value("d", 0.0, lock=False)
        pr = multiprocessing.Process(target=prepros.extract_rows_type,
                                     args=(df, uni_val, unique_col,))
        pr.start()
        pr.join()
        df_ship_type = ret_value.value
        print(df_ship_type)
        #df_ships = pd.concat([df_ships, df_ship_type])
        # df = prepros.remove_rows(df, uni_val, unique_col)
        # prepros.csv_out(df, "remaining.out")
    prepros.csv_out(df_ships, out_file)


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



            # prepros.csv_out(df_unique, out_file)
        # if rem_df:
        #    df = prepros.remove_rows(df, elem, column)
    # uniq = prepros.extract_uniq_val(df, 'MMSI')
    # search_mmsi(df, 'MMSI', uniq)


    # csv = file_h.read_csv(csv_file)
