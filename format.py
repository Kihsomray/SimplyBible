from datetime import datetime

books_edit = [["genesis", 50, 1533], ["exodus", 40, 1213], ["leviticus", 27, 859], ["numbers", 36, 1288], ["deuteronomy", 34, 959], ["joshua", 24, 658], ["judges", 21, 618],
         ["ruth", 4, 85], ["1 samuel", 31, 810],
         ["2 samuel", 24, 695], ["1 kings", 22, 816], ["2 kings", 25, 719], ["1 chronicles", 29, 942], ["2 chronicles", 36, 822], ["ezra", 10, 280], ["nehemiah", 13, 406], ["esther", 10, 167],
         ["job", 42, 1070], ["psalms", 150, 2461], ["proverbs", 31, 915], ["ecclesiastes", 12, 222], ["song of songs", 8, 117], ["isaiah", 66, 1292], ["jeremiah", 52, 1364], ["lamentations", 5, 154],
         ["ezekiel", 48, 1273], ["daniel", 12, 357], ["hosea", 14, 197], ["joel", 3, 73], ["amos", 9, 146], ["obadiah", 1, 21], ["jonah", 4, 48], ["micah", 7, 105], ["nahum", 3, 47], ["habakkuk", 3, 56],
         ["zephaniah", 3, 53], ["haggai", 2, 38], ["zechariah", 14, 211], ["malachi", 4, 55], ["matthew", 28, 1071], ["mark", 16, 678], ["luke", 24, 1151], ["john", 21, 879], ["acts", 28, 1007], ["romans", 16, 433],
         ["1 corinthians", 16, 437], ["2 corinthians", 13, 257], ["galatians", 6, 149], ["ephesians", 6, 155], ["philippians", 4, 104], ["colossians", 4, 95], ["1 thessalonians", 5, 89],
         ["2 thessalonians", 3, 47], ["1 timothy", 6, 113], ["2 timothy", 4, 83], ["titus", 3, 46], ["philemon", 1, 25], ["hebrews", 13, 303], ["james", 5, 108], ["1 peter", 5, 105],
         ["2 peter", 3, 61], ["1 john", 5, 105], ["2 john", 1, 13], ["3 john", 1, 14], ["jude", 1, 25], ["revelation", 22, 404]]

books = ["genesis", "exodus", "leviticus", "numbers", "deuteronomy", "joshua", "judges", "ruth", "1 samuel",
         "2 samuel", "1 kings", "2 kings", "1 chronicles", "2 chronicles", "ezra", "nehemiah", "esther",
         "job", "psalms", "proverbs", "ecclesiastes", "song of songs", "isaiah", "jeremiah", "lamentations",
         "ezekiel", "daniel", "hosea", "joel", "amos", "obadiah", "jonah", "micah", "nahum", "habakkuk",
         "zephaniah", "haggai", "zechariah", "malachi", "matthew", "mark", "luke", "john", "acts", "romans",
         "1 corinthians", "2 corinthians", "galatians", "ephesians", "philippians", "colossians", "1 thessalonians",
         "2 thessalonians", "1 timothy", "2 timothy", "titus", "philemon", "hebrews", "james", "1 peter",
         "2 peter", "1 john", "2 john", "3 john", "jude", "revelation"]

apocrypha_books = ["tobit", "judith"]

translations = ["cherokee", "bbe", "kjv", "web", "oeb-cw", "webbe", "oeb-us", "clementine", "almeida", "rccv"]

translation_guild = []


def format_trans(translation, guild_id):
    guild_id = str(guild_id)
    f_read = open("translations.txt", "r")
    lines = f_read.readlines()
    f_read.close()
    f_write = open("translations.txt", "a")
    f_write.truncate(0)
    for x in lines:
        if guild_id not in x:
            f_write.write(x)
    f_write.close()

    f_append = open("translations.txt", "a")
    f_append.write(guild_id + " " + translation + "\n")
    translation_guild.append([guild_id, translation])
    f_append.close()


def format_scrip(scripture):
    scripture = scripture.lower().replace(":", " ")
    split_scripture = scripture.split()
    book_string = split_scripture[0]
    chapter = "1"
    verse = ""
    if len(split_scripture) >= 5:
        return -1
    if not split_scripture[1].isnumeric():
        book_string = split_scripture[0] + " " + split_scripture[1]
        split_scripture[0] = split_scripture[0] + " " + split_scripture[1]
    if len(split_scripture) >= 2:
        if len(split_scripture) == 4 or not split_scripture[1].strip("-").isnumeric():
            if split_scripture[0].isnumeric():
                book_string = split_scripture[1]
            split_scripture[0] = split_scripture[0] + " " + split_scripture[1]
            split_scripture.pop(1)
        if len(split_scripture) >= 2:
            chapter = split_scripture[1]
    if len(split_scripture) >= 3:
        verse = ":" + split_scripture[2]
        verse_int = verse.replace(":", "").split("-")
        if len(verse_int) > 1:
            start = int(verse_int[0])
            end = int(verse_int[1])
            if end <= start:
                verse = ":" + str(max(1, start))
    book = book_string
    if book_string.strip("-").isnumeric():
        book = books[min(max(abs(int(book_string)), 1), 66) - 1]
    books_with_substring = [string for string in books if book in string]
    if len(books_with_substring) == 0:
        return -2
    else:
        for b in books_edit:
            if b[0] == books_with_substring[0]:
                if int(chapter) > int(b[1]):
                    chapter = str(b[1])
                    break
        scripture = books_with_substring[0].title() + " " + chapter.strip("-") + verse
        return scripture


def scripture_link(scripture):
    book = scripture.upper().replace(" ", "").replace("PHILIPPIANS", "PHP").replace("JUDGES", "JDG")[:3]
    book = book.replace("SON", "SNG").replace("EZE", "EZK").replace("JOE", "JOL").replace("PHI", "PHM")
    book = book.replace("NAH", "NAM").replace("MAR", "MRK").replace("JOH", "JHN").replace("JAM", "JAS")
    book = book.replace("1JO", "1JN").replace("2JO", "2JN").replace("3JO", "3JN")
    book_chapter = scripture[1:].split(":")[0]
    chapter = ""
    for c in book_chapter:
        if c.isdigit():
            chapter = chapter + c
    return "https://bible.com/bible/1/" + book + "." + chapter


def book_icon(scripture):
    scripture = scripture.lower()
    book = [string for string in books if string in scripture][0]
    if book == "1 samuel" or book == "2 samuel":
        book = "samuel"
    elif book == "1 kings" or book == "2 kings":
        book = "kings"
    elif book == "1 chronicles" or book == "2 chronicles":
        book = "chronicles"
    elif book == "song of songs":
        book = "song of solomon"
    elif book == "jonah":
        book = "Jonah"
    book = book.replace(" ", "-")
    link = "https://overviewbible.com/wp-content/uploads/2014/06/" + book + "-free-bible-icon-150x150.png"
    if book == "ruth" or book == "samuel" or book == "ezra" or book == "psalms" or book == "proverbs" or book == "philippians":
        link = "https://overviewbible.com/wp-content/uploads/2014/06/" + book + "-free-bible-icon.png-150x150.png"
    if book == "1-corinthians":
        link = "https://overviewbible.com/wp-content/uploads/2014/06/" + book + "300x300-150x150.png"
    return link


def get_guild_trans(guild_id):
    translation = "kjv"
    guild_id = str(guild_id)
    for x in translation_guild:
        if guild_id in x[0]:
            translation = x[1]
    return translation


def current_time():
    return datetime.now().strftime("%H:%M:%S")
