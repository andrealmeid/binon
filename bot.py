import telepot
from datetime import datetime
import time
from pprint import pprint
import pyowm

def getId(file):
    with open (file, "r") as file_id:
        return file_id.read().replace('\n', '')

def getWeather():
    owm = pyowm.OWM("e85982067df6a7e37f95e317f01ca80e")
    observation = owm.weather_at_place('sao paulo, br')
    w = observation.get_weather()
    status = w.get_detailed_status()
    temp_max = str(w.get_temperature('celsius')['temp_max'])
    temp_min = str(w.get_temperature('celsius')['temp_min'])
    temp_cur = str(w.get_temperature('celsius')['temp'])
    msg = "Bom dia!\nHoje Sao Paulo estara " + status
    msg += "\nAgora: " + temp_cur + "º\n"
    msg += "Maxima: " + temp_max + "º\n"
    msg += "Minima: " + temp_min + "º"
    return msg

bot_id = getId("id/bot.id")
me_id = getId("id/me.id")
gf_id = getId("id/gf.id")

bot = telepot.Bot(bot_id)

one_hour = 60*60
delay_time = one_hour

while True:
    current_hour = datetime.now().time().hour
    current_minute = datetime.now().time().minute

    if current_hour == 10 and current_minute == 0:
        weather_msg = getWeather()
        bot.sendMessage(me_id, weather_msg)
        bot.sendMessage(gf_id, weather_msg)
        time.sleep(delay_time)

    elif current_hour == 13 and current_minute == 0:
        bot.sendMessage(me_id, 'enviado')
        bot.sendMessage(gf_id, 'Hey xu, nao esquece de tomar a pilula! :)')
        time.sleep(delay_time)
    else:
        time.sleep(10)
