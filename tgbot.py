import os
import random
import time
import telegram
from environs import Env

from main import create_parser


def send_messages():
    parser = create_parser()
    parser.add_argument('time', default=14400, help="Введите время задержки отправления фото",
                        type=int)
    parser_args = parser.parse_args()
    document_dir = os.listdir("A:/Курс_DEVMAN/Lesson4_photo_to_tg/Photo_to_tg/images")
    while document_dir:
        random.shuffle(document_dir)
        for image in document_dir:
            path_to_file = f"A:/Курс_DEVMAN/Lesson4_photo_to_tg/Photo_to_tg/images/{image}"
            bot.send_document(chat_id=env.str("CHAT_ID"),
                              document=open(path_to_file, "rb"))
            time.sleep(parser_args.time)


if __name__ == "__main__":
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env.str("TG_BOT_TOKEN"))
    send_messages()
