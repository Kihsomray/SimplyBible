from datetime import datetime
from threading import Timer
import random
from query import *
from format import books_edit


important_verses = []
daily_scripture = "John 3:16"


#x = datetime.today()
#y = x.replace(day=x.day + 0, hour=0, minute=1, second=0, microsecond=0)
#delta_t = y - x

#secs = delta_t.seconds + 1

def get_daily():
    return important_verses[datetime.now().timetuple().tm_yday].replace("\n", "")


#def get_daily(scripture=random.randint(0, 369), *args, **kwargs):
    #daily_scripture = get_quote(important_verses[scripture], 0)


    #index = books_edit[scripture][0]
    #index_2 = books_edit[scripture][1]
    #url = "https://bible-api.com/{scripture} {chapter}".format(scripture=index, chapter=index_2)
    #response = requests.get(url)
    #json_data = json.loads(response.text)
    #verses = len(json_data['verses'])
    #url = "https://bible-api.com/{scripture} {chapter}:{verse}".format(scripture=index, chapter=index_2, verse=random.randint(0, verses))
    #response = requests.get(url)
    #json_data = json.loads(response.text)
    #global text
    #text = json_data["text"]
    #return text


#def access():
    #return text


#t = Timer(secs, get_daily)


#t.start()
