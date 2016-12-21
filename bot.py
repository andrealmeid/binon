import telepot
from datetime import datetime
import time
from pprint import pprint

with open ("id/bot.id", "r") as bot_file_id:
    bot_id = bot_file_id.read().replace('\n', '')

with open ("id/krauss.id", "r") as bot_file_id:
    krauss_id = bot_file_id.read().replace('\n', '')

with open ("id/tony.id", "r") as bot_file_id:
    tony_id = bot_file_id.read().replace('\n', '')

bot = telepot.Bot(bot_id)

# response = bot.getUpdates()
# pprint(response)

while 1:
    current_hour = datetime.now().time().hour
    current_minute = datetime.now().time().minute

    if current_hour >= 11 and current_minute >= 0:
        bot.sendMessage(tony_id, 'foi')
        bot.sendMessage(krauss_id, 'Hey xu, nao esquece de tomar a pilula! :)')
        print("foi")
    time.sleep(60*15)
