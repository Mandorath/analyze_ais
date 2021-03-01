"""Extract/pre-process data."""
import pandas as pd
import logging

log = logging.getLogger(__name__)


class PreProcess():
    """Preprocess data."""

    def __init__(self):
        self.frame = pd.DataFrame()

    def csv_to_df(self, file):
        """
        Set the dict to a dataframe.

        @file; string containing filename of the CSV file to read from.
        """
        df = pd.read_csv(file, index_col=None, header=0)
        return df

    def extract_rows_type(self, df, elem, column, remove, file_name):
        """
        Extract all rows based on value 'elem' in column 'column'.

        @elem: String that matches with a value in specified column.
        @column: Column that the value 'elem' should be matched.
        @df: Pandas dataframe
        @remove: Boolean, if true remove the rows after extraction from main
                 pandas dataframe.
        @file_name: The file the extracted rows should be written to.

        """
        log.info("Extracting rows with value {0} from column {1}".format(elem, column))
        df_base = df[df[column] == elem]
        self.csv_out(df_base, file_name)
        if remove:
            self.remove_rows(df, elem, column)
        return df

    def remove_rows(self, df, elem, column):
        """
        Remove the rows from the main pandas dataframe.

        @df: Pandas Dataframe
        @elem: String in rows that is matched for removel
        @column: String containing the column in which 'elem' should
                 be matched.
        """
        log.info("Removing rows with value {0} from column {1}".format(elem, column))
        df = df[df[column] == elem]
        return df

    def csv_out(self, df, filename):
        """
        Write Pandas dataframe to CSV file.

        @df: Pandas Dataframe
        @filename: String containing file name the dataframe should be
                   written to.
        """
        df.to_csv(filename)
