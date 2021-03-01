"""Extract/pre-process data."""
import fun_logger
import pandas as pd

log = fun_logger.getLogger(__name__)


class PreProcess():
    """Preprocess data."""

    def __init__(self):
        self.frame = pd.DataFrame()
        self.file_name = "basestation.csv"

    def csv_to_df(self, file):
        """Set the dict to a dataframe."""
        df = pd.read_csv(file, index_col=None, header=0)
        return df

    def extract_rows_type(self, df, elem, column, remove, file_name):
        log.info("Extracting rows with value {0} from column {1}".format(elem, column))
        df_base = df[df[column] == elem]
        self.csv_out(df_base, file_name)
        if remove:
            self.remove_rows(df, elem, column)

    def remove_rows(self, df, elem, column):
        log.info("removing rows with value {0} from column {1}".format(elem, column))
        df = df[df[column] == elem]

    def csv_out(self, df, filename):
        df.to_csv(filename)
