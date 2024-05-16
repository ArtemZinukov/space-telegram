import requests

from main import get_file_extension, create_parser


def fetch_spacex_last_launch():
    parser = create_parser()
    parser.add_argument('id', default="5eb87d47ffd86e000604b38a", help="Введите id запуска", type=str)
    parser_args = parser.parse_args()
    url = f"https://api.spacexdata.com/v5/launches/{parser_args.id}"
    response = requests.get(url)
    links = response.json()['links']['flickr']['original']
    for link_name, link in enumerate(links):
        file_extension = get_file_extension(link)
        filename = f"images/spacex{link_name}{file_extension}"
        response = requests.get(link)
        response.raise_for_status()
        with open(filename, "wb") as file:
            file.write(response.content)


if __name__ == "__main__":
    fetch_spacex_last_launch()
