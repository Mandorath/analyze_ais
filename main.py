#!/bin/python
"""Main script."""
import fun_logger
from extract import PreProcess
from command_line import parseOptions
from pro_yml import yaml_extract

log = fun_logger.init_log()

elem = "Base Station"
column = "Type of mobile"

if __name__ == '__main__':
    """Primary function."""
    parse_options = parseOptions()
    options = parse_options.arguments()
    # Configure logging
    fun_logger.handle_log(log, options.LOG)
    fun_logger.handle_console(log)

    prepros = PreProcess()

    csv_file = options.CSV
    out_file = options.OUTPUT
    df = prepros.csv_to_df(csv_file)
    df = prepros.extract_rows_type(df, elem, column, True, out_file)
    uniq = prepros.extract_uniq_val(df, 'MMSI')
    print(uniq)
    # csv = file_h.read_csv(csv_file)
