import requests
from environs import Env

from main import get_file_extension, create_parser


def fetch_nasa_apod():
    parser = create_parser()
    parser.add_argument('count', default=3, help="Введите количество фотографий, которые хотите вывести",
                        type=int)
    parser_args = parser.parse_args()
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": parser_args.count,
        "api_key": env.str("NASA_TOKEN")
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    response_data = response.json()
    for link_name, image in enumerate(response_data):
        url = image.get("url")
        file_extension = get_file_extension(url)
        filename = f"images/nasa_apod{link_name}{file_extension}"
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, "wb") as file:
            file.write(response.content)


if __name__ == "__main__":
    env = Env()
    env.read_env()
    fetch_nasa_apod()
