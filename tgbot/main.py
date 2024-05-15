import telegram


bot = telegram.Bot(token="6645877771:AAFXghs4k9Nzo6Br9BRUJVVlv2T1hXg8owA")


updates = bot.get_updates()
print(updates[-1])
bot.send_message(text="asdad", chat_id=-4271673960)
