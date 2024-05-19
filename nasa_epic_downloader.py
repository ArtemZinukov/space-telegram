import argparse
from datetime import datetime

import requests
from environs import Env

from scripts import writing_to_file


def fetch_nasa_epic(parser_arg, token):
    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": token
    }
    response = requests.get(url, params=params)
    decoded_response = response.json()
    downloaded_image = 0
    for image_name, image in enumerate(decoded_response):
        if downloaded_image >= parser_arg.count:
            break
        photo = image.get("image")
        date = image.get("date")
        formated_datetime = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date()
        formated_date = formated_datetime.strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{photo}.png"
        filename = f"images/nasa_epic{image_name}.png"
        writing_to_file(url, filename, params)
        downloaded_image += 1


def main():
    env = Env()
    env.read_env()
    parser = argparse.ArgumentParser(prog='Nasa_epic_downloader', description='Позволяет вывести нужное количество'
                                                                              'фотографий земли,')
    parser.add_argument('count', default=3, help="Введите количество фотографий, которые хотите вывести",
                        type=int)
    parser_arg = parser.parse_args()
    nasa_token = env.str("NASA_TOKEN")
    fetch_nasa_epic(parser_arg, nasa_token)


if __name__ == "__main__":
    main()
