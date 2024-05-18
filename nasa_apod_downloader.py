import argparse
import requests
from environs import Env

from scripts import get_file_extension, writing_to_file


def fetch_nasa_apod():
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": parser_args.count,
        "api_key": nasa_token
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    decoded_response = response.json()
    for link_name, image in enumerate(decoded_response):
        url = image.get("url")
        file_extension = get_file_extension(url)
        filename = f"images/nasa_apod{link_name}{file_extension}"
        writing_to_file(url, filename)


if __name__ == "__main__":
    env = Env()
    env.read_env()
    parser = argparse.ArgumentParser(prog='Nasa_apod_downloader', description='Позволяет вывести определенное '
                                                                              'количество каждодневных фотографии nasa')
    parser.add_argument('count', default=3, help="Введите количество фотографий, которые хотите вывести",
                        type=int)
    parser_args = parser.parse_args()
    nasa_token = env.str("NASA_TOKEN")
    fetch_nasa_apod()
