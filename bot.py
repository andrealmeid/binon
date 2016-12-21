import telepot
from pprint import pprint

with open ("bot.id", "r") as bot_file_id:
    bot_id = bot_file_id.read().replace('\n', '')

bot = telepot.Bot(bot_id)

response = bot.getUpdates()
pprint(response)
