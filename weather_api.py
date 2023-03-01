# import requests
# import json

# x = requests.get('http://www.7timer.info/bin/astro.php?lon=113.17&lat=23.09&ac=0&lang=en&unit=metric&output=json&tzshift=0')
# data = json.loads(x.text)
# print(data['dataseries'][0]['wind10m']['direction'])

# Just learning how to consume APIs.
# API: 7timer weather API
# Monday 27th February 2023

import argparse
from configparser import ConfigParser

def _get_api_key() -> str:
    """Fetch the API key from your configuration file.

    Expects a configuration file named "secrets.ini" with structure:

        [openweather]
        api_key=<YOUR-OPENWEATHER-API-KEY>
    """
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]
# print(_get_api_key())
def read_user_cli_args() -> str:
    """Handles the CLI user interactions.

    Returns:
        argparse.Namespace: Populated namespace object
    """
    parser = argparse.ArgumentParser(
        description="gets weather and temperature information for a city"
    )
    parser.add_argument(
        "city", nargs="+", type=str, help="enter the city name"
    )
    parser.add_argument(
        "-i",
        "--imperial",
        action="store_true",
        help="display the temperature in imperial units",
    )
    return parser.parse_args()

if __name__ == "__main__":
    read_user_cli_args()