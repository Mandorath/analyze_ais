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

        Args:
            file (str); Contains filename of the CSV file to read from.

        """
        df = pd.read_csv(file, index_col=None, header=0)
        return df

    def extract_uniq_val(self, df, column):
        """
        Find rows that matche string @elem in column @column.

        Args:
            elem (str): String to match when searching rows.
            column (str): Contains name of the column to match the string.
            df (df): Pandas dataframe

        """
        unique_val = df[column].unique()
        return unique_val

    def find_rows(self, df, elem, column):
        """
        Find rows that matche string @elem in column @column.

        Args:
            elem (str): String to match when searching rows.
            column (str): Contains name of the column to match the string.
            df (df): Pandas dataframe

        """
        log.info("Creating new dataframe matching value {0} in column {1}".format(elem, column))
        df_base = df[df[column] == elem]
        return df_base

    def extract_rows_type(self, df, elem, column, remove, file_name):
        """
        Extract all rows based on value 'elem' in column 'column'.

        Args:
           elem (str): String, that matches with a value in specified column.
           column (str): Contains name of the column that the value 'elem'
                         should be matched.
           df: Pandas dataframe
           remove (bool): If true remove the rows from the dataframe
                          after extraction from main pandas dataframe.
           file_name (str): The file the extracted rows should be written to.

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

        Args:
          df (df): Pandas Dataframe
          elem (str): String used in rows that is matched for removal
          column (str): Contains the column in which 'elem' should
                        be matched.

        """
        log.info("Removing rows with value {0} from column {1}".format(elem, column))
        df = df[df[column] == elem]
        return df

    def csv_out(self, df, filename):
        """
        Write Pandas dataframe to CSV file.

        Args:
            df: Pandas Dataframe
            filename: Contains file name the dataframe should be written to.

        """
        log.info("Writing to CSV file {0}".format(filename))
        df.to_csv(filename)
