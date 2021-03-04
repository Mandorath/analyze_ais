#!/bin/python
"""Main script."""
import fun_logger
import ruamel.yaml
from extract import PreProcess
from command_line import parseOptions
from pro_yml import yaml_extract
# from search_ais_gaps import search_ais_gaps

log = fun_logger.init_log()
yml_tst = ruamel.yaml

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
    for extract in instruct['extract']:
        print(yml_tst.safe_dump(extract))
        elem = extract['elem']
        column = extract['column']
        out_file = extract['out_file']
        rem_df = extract['remove_in_df']
        df, df_base = prepros.extract_rows_type(df, elem, column)
        prepros.csv_out(df_base, out_file)
        if rem_df:
            df = prepros.remove_rows(df, elem, column)

    for extract in instruct['extract_vessel_types']:
        print(yml_tst.safe_dump(extract))
        elem = extract['elem']
        column = extract['column']
        out_file = extract['out_file']
        rem_df = extract['remove_in_df']
        unique_col = extract['unique_column']
        df, df_base = prepros.extract_rows_type(df, elem, column)
        df_unique = prepros.extract_uniq_val(df_base, unique_col)
        prepros.csv_out(df_base, out_file)
        # if rem_df:
        #    df = prepros.remove_rows(df, elem, column)
    # uniq = prepros.extract_uniq_val(df, 'MMSI')
    # search_mmsi(df, 'MMSI', uniq)


    # csv = file_h.read_csv(csv_file)
