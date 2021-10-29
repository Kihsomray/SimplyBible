import json

import requests
from format import *

API_KEY = "6b311ec73be90751e7528d34c0823ef9"

# Genesis 30:1 - specific verse, proper arg
# ex 3 1 - specific verse, short arg
# psa 1 - entire chapter


def get_quote(scripture, guild_id, user_id=0, *args, **kwargs):
    translation = get_guild_trans(guild_id)
    url = "https://bible-api.com/{scripture}?translation={translation}".format(scripture=scripture, translation=translation)
    response = requests.get(url)
    json_data = json.loads(response.text)
    #print(json_data)
    try:
        out = [""]
        index = 0
        for v in json_data['verses']:
            if len(out[index] + "**" + str(v["verse"]) + ".** " + v["text"].replace("\n", " ").strip() + str(get_note(str(user_id), str(v["book_name"]) + " " + str(v["chapter"]) + ":" + str(v["verse"])))) > 4093:
                index += 1
                out.append("")
            out[index] += "**" + str(v["verse"]) + ".** " + v["text"].replace("\n", " ").strip() + get_note(str(user_id), str(v["book_name"]) + " " + str(v["chapter"]) + ":" + str(v["verse"]))

        return out
    except:
        verses = fix_verses(scripture)
        if verses == scripture:
            return -3
        else:
            return get_quote(verses, guild_id)


def fix_verses(scripture):
    verse = scripture.split(":")
    if len(verse) > 1:
        chapter = verse[0]

        json_data = json.loads(requests.get("https://bible-api.com/{scripture}".format(scripture=chapter)).text)
        verse_amt = len(json_data["verses"])
        verses = verse[1].split("-")
        start = int(verses[0])
        end = start
        if len(verses) == 2:
            end = int(verses[1])
        if start > verse_amt:
            start = verse_amt
        if end > verse_amt:
            end = verse_amt

        return format_scrip(chapter + ":" + str(start) + "-" + str(end))
    else:
        return scripture
