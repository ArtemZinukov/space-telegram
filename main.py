import argparse
import os.path
from urllib.parse import urlparse


def get_file_extension(url):
    url_parse = urlparse(url)
    file_extension = os.path.splitext(url_parse.path)
    return file_extension[1]


def create_parser():
    parser = argparse.ArgumentParser()
    return parser
