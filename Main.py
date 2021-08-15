import discord

from discord.ext.commands import Bot

import json

from Wikipedia import *

from Math import *

from MorseCode import *

def ChangeLanguage(Guild, Language):
    with open("ServerLanguage.json", 'w') as f:
        dicto = json.load(f)
        dicto[Guild] = Language
        json.dump(dicto, f)
        f.close()
    return None

def ReturnLanguage(Guild):
    with open("ServerLanguage.json", 'r') as f:
        dicto = json.load(f)
        f.close()
    if dicto.get(Guild) == None:
        return 'en'
    return dicto.get(Guild)
Bot = Bot(command_prefix='~')  # sets the prefix

@Bot.event
async def on_ready():
    await Bot.change_presence(status=discord.Status.online, activity=discord.Game("Waiting to help you"))
    print("Online")


@Bot.event  # message function
async def on_message(message):
    Message = str(message.content)
    print(Message[0:18])
    if Message[0:10] == "~wikipedia":
        WordStep1 = Message.split(" ")
        Word = WordStep1[2:]
        Word = " ".join(Word)
        Language = ReturnLanguage(message.guild)
        if message.startswith("~wikipedia summary"):
            Result = Summary(Word, Language)
            await message.channel.send(Result)

        elif message.startswith("~wikipedia search"):
            Result = search(Word, Language)
            await message.channel.send(Result)

        elif message.startswith("~wikipedia reference"):
            Result = reference(Word, Language)
            await message.channel.send(Result)

        elif message.startswith("~wikipedia random"):
            Result = Random(Language)
            await message.channel.send(Result)

        elif message.startswith("~wikipedia image"):
            Result = Images(Word)
            await message.channel.send(Result)

        elif message.startswith("~wikipedia categories"):
            Result = Categories(Word, Language)
            await message.channel.send(Result)

        elif message.startswith("~wikipedia link"):
            Result = Link(Word, Language)
            await message.channel.send(Result)

        elif message.startswith("~wikipedia test"):
            Result = Test(Word, Language)
            await message.channel.send(Result)

        elif message.startswith("~wikipedia section"):
            Result = Section(Word, Language)
            await message.channel.send(Result)

        elif message.startswith("~wikipedia url"):
            Result = url(Word, Language)
            await message.channel.send(Result)

        elif message.startswith("~wikipedia simple"):
            Result = Simple(Word, Language)
            await message.channel.send(Result)

        else:
            await message.channel.send("Invalid Command")



    elif message.startswith("~math"):
        pass
    elif message.startswith("~morse"):
        pass

Bot.run("ODQ4NDc0OTA5MTU0NzM4MjA2.YLNJ1g.tdzcgXxlLGWG7bSqVXK5Ic3TTUA")
