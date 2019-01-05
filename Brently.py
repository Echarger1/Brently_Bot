import discord
from discord.ext import commands
import random
import webCrawler
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_message(message):

    # we do not want the bot to reply to itself
    if message.author == bot.user:

        return

    if message.content.upper().startswith('!HELLO'):

        msg = 'Screw you! {0.author.mention}'.format(message)

        await bot.send_message(message.channel, msg)

    if message.content.upper().startswith('!KICK'):
        membs = bot.get_all_members()
        print(message.content)
        for mem in membs:
            print(mem.name)
            print(message.content[6:])
            if mem.name == message.content[6:]:
                print("attempting to kick")
                await bot.kick(mem)
                break

    if message.content.upper().startswith('!BAN'):
        ban_membs = bot.get_all_members()
        print(message.content)
        for ban_mem in ban_membs:
            print(ban_mem.name)
            print(message.content[5:])
            if ban_mem.name == message.content[5:]:
                await bot.ban(ban_mem)
                msg = 'I will bring down the mighty BANHAMMER upon them my lord!'.format(message)
                await bot.send_message(message.channel, msg)
                break
    

    #adding command for meme
    if message.content.upper().startswith("!MEME"):
        meme = webCrawler.get_meme()
        await bot.send_message(message.channel, meme)
     #wiki logic
    if message.content.upper().startswith("!WIKI"):
        command = message.content[6:]
        url = wiki.search(command)
        await bot.send_message(message.channel, url)

@bot.event
async def on_ready():

    print('Logged in as')

    print(bot.user.name)

    print(bot.user.id)

    print('------')

bot.run('NTMwOTEwMTg5NzA1MjMyNDI0.DxGQnw.L79pM1WpTX4qY_FnrogrUwT4-z4')