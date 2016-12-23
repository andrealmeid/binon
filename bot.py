import telepot
from datetime import datetime
import time
from pprint import pprint

def getId(file):
    with open (file, "r") as file_id:
        return file_id.read().replace('\n', '')

bot_id = getId("id/bot.id")
me_id = getId("id/me.id")
gf_id = getId("id/gf.id")

bot = telepot.Bot(bot_id)

delay_time = 60*30

while 1:
    current_hour = datetime.now().time().hour
    current_minute = datetime.now().time().minute

    #please notice there is no caution with time precision here
    if current_hour >= 11 and current_minute >= 0:
        bot.sendMessage(me_id, 'enviado')
        bot.sendMessage(gf_id, 'Hey xu, nao esquece de tomar a pilula! :)')
    time.sleep(delay_time)
