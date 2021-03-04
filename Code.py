import os

import discord

from dotenv import load_dotenv

from discord.ext import commands

import wikipedia

import nest_asyncio
nest_asyncio.apply()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix = '!!')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Prefix !!"))
    print("Ran")


@bot.event
async def on_member_join (member):

        await member.create_dm()
        await member.dm_channel.send (f'Hi {member.name}, welcome to my Discord server!')



@bot.event
async def on_message(message):
    Stringo = message.content
    if Stringo[0:2] == '!!':
        if Stringo == "!!syntax" or Stringo == "!!help":
            help_msg = "First, type !!search{topic}, after that find the topic you want to search about, after that, type !!{topic}{number of sentences}, and the result will be printed out"
            await message.channel.send(help_msg)
        elif message.content.startswith("!!search"):
            search = Stringo[8:]
            result = wikipedia.search(search, 20)
            await message.channel.send(result)
        elif message.content.startswith("!!page"):
            search = Stringo[6:]
            result = wikipedia.page(search, preload=True)
            await message.channel.send(result)
        elif message.content.startswith("!!random"):
            result = wikipedia.random(pages = 1)
            await message.channel.send(result)
        else:
            try:
                num = int(Stringo[-1])
                search = Stringo[2:len(Stringo) - 1]
                sentence = num
                result = wikipedia.summary(search, sentence)

                await message.channel.send(result)
            except:
                num = 5
                search = Stringo[2:len(Stringo) - 1]
                sentence = num
                result = wikipedia.summary(search, sentence)
                await message.channel.send(result)



bot.run(TOKEN)
