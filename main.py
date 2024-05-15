from datetime import datetime
import os.path

import requests
from urllib.parse import urlparse


def get_file_extension(url):
    url_parse = urlparse(url)
    file_extension = os.path.splitext(url_parse.path)
    return file_extension[1]


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url)
    links = response.json()['links']['flickr']['original']
    for link_name, link in enumerate(links):
        file_extension = get_file_extension(link)
        filename = f"images/spacex{link_name}{file_extension}"
        response = requests.get(link)
        response.raise_for_status()
        with open(filename, "wb") as file:
            file.write(response.content)


def fetch_nasa_apod():
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": 40,
        "api_key": "j1rhVwMxoiYAntp852yppqRSIxCEjeYaJCtng0Sg"
    }
    response = requests.get(url, params=params)
    response_data = response.json()
    for link_name, image in enumerate(response_data):
        url = image.get("url")
        file_extension = get_file_extension(url)
        filename = f"images/nasa_apod{link_name}{file_extension}"
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, "wb") as file:
            file.write(response.content)


def fetch_nasa_epic(count):
    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": "j1rhVwMxoiYAntp852yppqRSIxCEjeYaJCtng0Sg"
    }
    response = requests.get(url, params=params)
    response_data = response.json()
    dowload_image = 0
    for image_name, image in enumerate(response_data):
        if dowload_image >= count:
            break
        photo = image.get("image")
        date = image.get("date")
        adate = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date()
        formated_date = adate.strftime("%Y/%m/%d")
        url = (f"https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png"
               f"/{photo}.png?api_key=j1rhVwMxoiYAntp852yppqRSIxCEjeYaJCtng0Sg")
        filename = f"images/nasa_epic{image_name}.png"
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, "wb") as file:
            file.write(response.content)
            dowload_image += 1
