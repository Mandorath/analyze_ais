"""Class for handling files."""
import csv
import logging

log = logging.getLogger(__name__)


class FileHandle():
    """Generic functions for reading files."""

    def __init__(self):
        """Intial class."""
        pass

    def read_csv(self, file):
        """For all csv files extract data."""
        log.info("Opening csv file {0}".fornat(file))
        with open(file) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            return csv_reader
