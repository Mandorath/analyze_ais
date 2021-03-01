"""Process yaml data."""
import ruamel.yaml
import logging

yml = ruamel.yaml

log = logging.getLogger(__name__)


class yaml_replacer():
    """Modify yaml dicts using ruamel."""

    def __init__(self):
        """Constructor for class."""

    def read_file(self, yaml_file):
        """Construct a new YamlDoc instance based on the given file.
        Args:
            yaml_file (str): string containing the locaiton of a file
            containing yaml data.
            yml_file (dict): Dictionary containing the yaml data that is read
            from the file.

        An exception is raised if the file is invalid or cannot be read.
        """
        try:
            with open(yaml_file, "r") as f:
                yml_file = yml.safe_load(f)
                return yml_file
        except IOError as e:
            raise Exception('Failed to read YAML file: "{0}"; {1}'
                            .format(yaml_file, e))
        except yml.YAMLError as e:
            raise Exception('Failed reading content of YAML file: '
                            '"{0}"; {1}'.format(yaml_file, e))


    def write_to_file(self, file, dump):
        """Write yaml dictionary to file."""
        log.debug(dump)
        with open(file, 'w') as fp:
            yml.round_trip_dump(dump, fp, block_seq_indent=2)
