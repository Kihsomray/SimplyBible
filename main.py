# Accessing the discord
import discord

from query import *
from format import *
from datetime import datetime
from daily import *
from toc import get_content
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

prefix = "!"

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='people type !bible'))
    print("[" + current_time() + "] Logged in as {0.user}".format(client))
    f_read = open("translations.txt", "r")
    for x_line in f_read:
        split = str(x_line).split(" ")
        translation_guild.append([split[0], split[1].replace("\n", "")])
    f_read.close()

    d_read = open("daily.txt", "r")
    for y_line in d_read:
        important_verses.append(y_line)
    d_read.close()
    get_daily()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try_again = " Please try again!"

    if message.content.lower().startswith(prefix + 'bible ver') or message.content.lower().startswith(prefix + 'bib ver'):
        print("[" + current_time() + "] " + message.author.name + " @ " + message.guild.name + " (" + str(message.guild.id) + "): " + message.content)
        start_time = datetime.now().microsecond
        split_string = message.content.split(" ")
        if len(split_string) == 2:
            split_string.append("list")
        embed = discord.Embed(timestamp=datetime.utcnow())
        footer_string = "Requested"
        if len(split_string) == 3:
            version = split_string[2].lower()
            if version in translations:
                format_trans(version, message.guild.id)
                embed = discord.Embed(description="Successfully Changed Translation to **" + version.upper() + "**", color=0x00ff00)
                embed.set_author(name="Settings", icon_url="https://i.imgur.com/VWP2TLc.png")
                footer_string = "Set"
            elif version == "list":
                section = "You can switch between multiple Bible translations. Only public domain Bibles " \
                          "are currently available.\n\nSwitch to a translation using **!bible version <prefix>**." \
                          "\n\n__Translations include:__"
                embed = discord.Embed(description=section, color=0x00ff00, timestamp=datetime.utcnow())
                embed.add_field(name='KJV', value="King James Version [EN]", inline=True)
                embed.add_field(name='WEB', value="World English Bible [EN]", inline=True)
                embed.add_field(name='BBE', value="Bible in Basic English [EN]", inline=True)
                embed.add_field(name='OEB-US', value="Open English Bible (US Edition) [EN]", inline=True)
                embed.add_field(name='OEB-CW', value="Open English Bible (CW Edition) [EN]", inline=True)
                embed.add_field(name='WEBBE', value="World English Bible, (British Edition) [EN]", inline=True)
                embed.add_field(name='CHEROKEE', value="Cherokee New Testament [CR]", inline=True)
                embed.add_field(name='CLEMENTINE', value="Clementine Latin Vulgate [LA]", inline=True)
                embed.add_field(name='ALMEIDA', value="João Ferreira de Almeida [PT]", inline=True)
                embed.add_field(name='RCCV', value="Romanian Corrected Cornilescu Version [RO]", inline=True)
                embed.set_author(name="Switching Bible Translation", icon_url="https://i.imgur.com/DA8lgY0.png")
            else:
                embed = discord.Embed(title="Error", description="Invalid translation!" + try_again, color=0xff0000)
        else:
            embed = discord.Embed(title="Error", description="Invalid use of command!" + try_again, color=0xff0000)
        embed.set_footer(text=footer_string + " by {name}".format(name=message.author.name),
                         icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        print("[" + current_time() + "] Response in " + str(abs(round((datetime.now().microsecond - start_time) / 1000))) + "ms")

    elif message.content.lower().startswith(prefix + 'bible daily') or message.content.lower().startswith(prefix + 'bib daily'):
        print("[" + current_time() + "] " + message.author.name + " @ " + message.guild.name + " (" + str(message.guild.id) + "): " + message.content)
        start_time = datetime.now().microsecond
        location = format_scrip(get_daily())
        quote = get_quote(location, message.guild.id)
        new_quote = ""
        for section in quote:
            new_quote += section + " "
        embed = discord.Embed(description=new_quote, color=0x00ff00, timestamp=datetime.utcnow())
        embed.set_author(name=location + " [" + get_guild_trans(message.guild.id).upper() + "] (Today's Verse)",
                         url=scripture_link(location), icon_url=book_icon(location))
        embed.set_footer(text="Requested by {name}".format(name=message.author.name),
                         icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        print("[" + current_time() + "] Response in " + str(abs(round((datetime.now().microsecond - start_time) / 1000))) + "ms")

    elif message.content.lower().startswith(prefix + 'bib toc') or message.content.lower().startswith(prefix + 'bible toc') or message.content.lower().startswith(prefix + 'bible tableofcontent'):
        print("[" + current_time() + "] " + message.author.name + " @ " + message.guild.name + " (" + str(message.guild.id) + "): " + message.content)
        start_time = datetime.now().microsecond
        if "simple" in message.content:
            await message.channel.send(embed=get_content(discord, message.author))
        else:
            s = ['#    Book        Chapters  Verses']
            index = 1
            for data in books_edit:
                space = 16
                start = '   '
                for item in data:
                    start += str(item).ljust(space, ' ')
                    space = 6
                str_index = str(index)
                if index < 10:
                    str_index += ' '
                s.append((str_index + start).title())
                index += 1
            d = '```' + '\n'.join(s) + '```'
            embed = discord.Embed(title='Bible - Table of Content', description=d, timestamp=datetime.utcnow(), color=0x00ff00)
            embed.set_footer(text="Requested by {name}".format(name=message.author.name),
                             icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
            print("[" + current_time() + "] Response in " + str(abs(round((datetime.now().microsecond - start_time) / 1000))) + "ms")

    elif message.content.lower().startswith(prefix + "bib"):
        str_message = message.content
        print("[" + current_time() + "] " + message.author.name + " @ " + message.guild.name + " (" + str(message.guild.id) + "): " + str_message)
        start_time = datetime.now().microsecond

        if "help" in str_message:
            str_message = "!bib"

        if " " in str_message:
            embed = discord.Embed(timestamp=datetime.utcnow())
            try:
                scripture = format_scrip(str_message.split(" ", 1)[1])
                print("[" + current_time() + "] Corrected: " + scripture)
                if scripture == -1:
                    embed = discord.Embed(title="Error", description="Invalid verse!" + try_again, color=0xff0000)
                elif scripture == -2:
                    embed = discord.Embed(title="Error", description="Invalid chapter!" + try_again, color=0xff0000)
                else:
                    quote = get_quote(scripture, message.guild.id)
                    if quote == -3:
                        embed = discord.Embed(title="Error", description="Invalid location of scripture!" + try_again,
                                              color=0xff0000)
                    else:
                        new_quote = get_quote(scripture, message.guild.id)
                        fixed_scripture = fix_verses(scripture)
                        if fixed_scripture == -1:
                            fixed_scripture = "Song of Songs"
                        index = 0
                        for section in new_quote:
                            embed = discord.Embed(description=section, color=0x00ff00)
                            if index == len(new_quote) - 1:
                                embed = discord.Embed(description=section, color=0x00ff00, timestamp=datetime.utcnow())
                                embed.set_footer(text="Requested by {name}".format(name=message.author.name),
                                                 icon_url=message.author.avatar_url)
                            if index == 0:
                                translation = get_guild_trans(message.guild.id)
                                embed.set_author(name=fixed_scripture + " [" + translation.upper() + "]", url=scripture_link(scripture),
                                                 icon_url=book_icon(scripture))
                            await message.channel.send(embed=embed)
                            index += 1
                        print("[" + current_time() + "] Response in " + str(abs(round((datetime.now().microsecond - start_time) / 1000))) + "ms")
                        return
            except:
                embed = discord.Embed(title="Error", description="Invalid location of scripture!" + try_again, color=0xff0000)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text="Requested by {name}".format(name=message.author.name), icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
            print("[" + current_time() + "] Response in " + str(abs(round((datetime.now().microsecond - start_time) / 1000))) + "ms")
        else:
            section = "There are a handful of ways to look up scripture using Bible (Discord bot).\n\n" \
                      "You can specify the book as the name of the book or the number of the book. " \
                      "You may even request to read a whole chapter by only mentioning the chapter or a specific " \
                      "(set of) verses. \n\n__Here are some examples:__\n\n**!bib psa 23:1-6** - Psalms 23:1-6" \
                      "\n**!bible 40 16** - Matthew 16:1-28 \n**!bible -66 -1 6** - Revelations 1:6" \
                      "\n**!bib Genesis 4 10-14** - Genesis 4:10-14\n\n__Adjust Settings:__\n\n**!bible version list**" \
                      " - List of translations available.\n**!bible version <prefix>** - Switch to a translation."
            embed = discord.Embed(description=section, color=0x00ff00, timestamp=datetime.utcnow())
            embed.set_thumbnail(url=client.user.avatar_url)
            embed.set_footer(text="Requested by {name}".format(name=message.author.name), icon_url=message.author.avatar_url)
            embed.set_author(name="How to Use Bible Discord Bot", icon_url="https://i.imgur.com/DA8lgY0.png")
            await message.channel.send(embed=embed)
            print("[" + current_time() + "] Response in " + str(abs(round((datetime.now().microsecond - start_time) / 1000))) + "ms")

    #elif message.content.startswith(prefix + "verseoftheday"):
    #    await message.channel.send(access())

# Run the client
client.run(TOKEN)
