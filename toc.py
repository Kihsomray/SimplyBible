from format import books_edit
from datetime import datetime


def get_content(discord, author):
    index = 1
    number = ""
    books = ""
    chapters = ""
    for book in books_edit:
        number += str(index) + "\n"
        books += book[0].title() + "\n"
        chapters += str(book[1]) + "\n"
        index += 1
    embed = discord.Embed(title="Bible - Table of Content", color=0x00ff00, timestamp=datetime.utcnow())
    embed.add_field(name='#', value=number, inline=True)
    embed.add_field(name='book', value=books, inline=True)
    embed.add_field(name='chapters', value=chapters, inline=True)
    embed.set_footer(text="Requested by {name}".format(name=author.name),
                     icon_url=author.avatar_url)
    return embed