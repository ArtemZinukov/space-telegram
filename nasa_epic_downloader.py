import requests
from environs import Env
from datetime import datetime

from main import create_parser


def fetch_nasa_epic():
    parser = create_parser()
    parser.add_argument('count', default=3, help="Введите количество фотографий, которые хотите вывести",
                        type=int)
    parser_arg = parser.parse_args()
    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": env.str("NASA_TOKEN")
    }
    response = requests.get(url, params=params)
    response_data = response.json()
    download_image = 0
    for image_name, image in enumerate(response_data):
        if download_image >= parser_arg.count:
            break
        photo = image.get("image")
        date = image.get("date")
        formated_datetime = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date()
        formated_date = formated_datetime.strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{photo}.png"
        filename = f"images/nasa_epic{image_name}.png"
        response = requests.get(url, params=params)
        response.raise_for_status()
        with open(filename, "wb") as file:
            file.write(response.content)
            download_image += 1


if __name__ == "__main__":
    env = Env()
    env.read_env()
    fetch_nasa_epic()
