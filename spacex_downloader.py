import argparse
import requests

from scripts import get_file_extension, write_to_file


def fetch_spacex_last_launch(launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    links = response.json()['links']['flickr']['original']
    for link_name, link in enumerate(links):
        file_extension = get_file_extension(link)
        filename = f"images/spacex{link_name}{file_extension}"
        write_to_file(link, filename)


def main():
    parser = argparse.ArgumentParser(prog='Spacex_downloader', description='Позволяет загрузить фотографии'
                                                                           ' spacex по id запуска')
    parser.add_argument('id', default="5eb87d47ffd86e000604b38a", help="Введите id запуска", type=str)
    parser_args = parser.parse_args()
    fetch_spacex_last_launch(parser_args.id)


if __name__ == "__main__":
    main()
