import argparse
import os
import random
import time
import telegram
from environs import Env


def send_messages(bot, chat_id, parser_args):
    document_dir = os.listdir("./images")
    while document_dir:
        random.shuffle(document_dir)
        for image in document_dir:
            path_to_file = f"./images/{image}"
            with open(path_to_file, "rb") as file:
                document = file.read()
            bot.send_document(chat_id=chat_id,
                              document=document)
            time.sleep(parser_args.time)


def main():
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env.str("TG_BOT_TOKEN"))
    parser = argparse.ArgumentParser(prog='tgbot', description='запускает тг бота, для отправки фотографий')
    parser.add_argument('time', default=14400, help="Введите время задержки отправления фото",
                        type=int)
    parser_args = parser.parse_args()
    tg_chat_id = env.str("TG_CHAT_ID")
    send_messages(bot, tg_chat_id, parser_args)


if __name__ == "__main__":
    main()
