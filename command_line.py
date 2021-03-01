"""Class for command line arguments."""
import argparse


class parseOptions():
    """Parse arguments."""

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='''CSV extraction
                                                             conversion''')

    def arguments(self):
        """Command line options."""
        self.parser.add_argument(
                '--csv',
                dest="CSV",
                action="store",
                default='ais.csv',
                help="""
                Specify the csv file that will be used.
                """,
                required=True,
            )
        self.parser.add_argument(
                '--output-file-name',
                dest="OUTPUT",
                action="store",
                default="desktop",
                help="""
                Specify csv output file.
                """,
                required=False,
            )
        self.parser.add_argument(
                '--log-file',
                dest="LOG",
                action="store",
                default="ais_parse.log",
                help="""
                Specify log file.
                Defaults to ais_pars.log in local directory.
                """,
                required=False,
            )
        args = self.parser.parse_args()
        return args
