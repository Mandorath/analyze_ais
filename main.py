"""Main script."""
import fun_logger
from man_file import FileHandle
from extract import PreProcess
from command_line import parseOptions

log = fun_logger.init_log()

elem = "Base Station"
column = "Type of mobile"

if __name__ == '__main__':
    """Primary function."""
    parse_options = parseOptions()
    options = parse_options.arguments()
    fun_logger.handle_log(log, options.LOG)
    fun_logger.handle_console(log)

    file_h = Filehandle()
    prepros = PreProcess()

    csv_file = options.CSV
    out_file = options.OUTPUT
    df = prepos.csv_to_df(csv_file)
    df = prepos.extract_rows_type(df, elem, column, True, out_file)
    # csv = file_h.read_csv(csv_file)
