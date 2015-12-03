"""
YAEP - Yet Another Environment Package

"""

import os
import ConfigParser
from utils import SectionHeader


boolean_map = {
    True: ['True', '1'],
    False: ['False', '0']
}


def env(key, default=None, convert_booleans=True, sticky=False):
    """
    Retrieves key from the environment.
    """
    value = os.getenv(key, default)

    if sticky and value == default:
        os.environ[key] = str(value)

    if convert_booleans and isinstance(value, str):
        value = str_to_bool(value)

    return value


def str_to_bool(string):
    for boolean in boolean_map:
        if any(string.lower() == val.lower() for val in boolean_map[boolean]):
            return boolean

    return string


def populate_env(env_file='.env'):
    env_file = os.getenv('ENV_FILE', env_file)

    if os.path.exists(env_file):
        with open(env_file) as ef:
            env_data = ConfigParser.SafeConfigParser()
            env_data.optionxform = str
            env_data.readfp(SectionHeader(ef))

        for key, value in env_data.items(SectionHeader.header):
            os.environ[key] = str(value)
