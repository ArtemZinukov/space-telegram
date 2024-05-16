import telegram

from environs import Env

env = Env()
env.read_env()

bot = telegram.Bot(token=env.str("TG_BOT_TOKEN"))
updates = bot.get_updates()
print(updates[-1])

bot.send_document(chat_id=-4271673960,
                  document="https://api.nasa.gov/EPIC/archive/natural/2024/"
                           "05/14/png/epic_1b_20240514003633.png?api_key=DEMO_KEY")
