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

one_hour = 60*60
delay_time = 24*one_hour

while 1:
    current_hour = datetime.now().time().hour
    current_minute = datetime.now().time().minute

    if current_hour == 13 and current_minute == 0:
        bot.sendMessage(me_id, 'enviado')
        #bot.sendMessage(gf_id, 'Hey xu, nao esquece de tomar a pilula! :)')
        time.sleep(delay_time)
    else:
        time.sleep(10)
