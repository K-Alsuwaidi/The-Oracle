import os

import discord

from discord.ext import commands

import wikipedia

import nest_asyncio
nest_asyncio.apply()


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
        elif message.content.startswith("!!search"): #7
            search = Stringo[8:]
            print(search)
            result = wikipedia.search(search, 20)
            await message.channel.send(result)
        else:
            try:
                num = int(Stringo[-1])
                search = Stringo[2:len(Stringo) - 1]
                sentence = num
                result = wikipedia.summary(search, sentence)

                await message.channel.send(result)
            except:
                pass




bot.run(TOKEN)
