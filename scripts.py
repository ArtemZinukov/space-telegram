import os.path
import requests
from urllib.parse import urlparse


def get_file_extension(url):
    url_parse = urlparse(url)
    file_extension = os.path.splitext(url_parse.path)
    return file_extension[1]


def writing_to_file(url, filename, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filename, "wb") as file:
        file.write(response.content)
