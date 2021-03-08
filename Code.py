
import discord

from discord.ext import commands

import wikipedia

bot = commands.Bot(command_prefix = '!!')

@bot.event
async def on_ready():
    game = discord.Game("Browing Wikipedia, Prefix: !!")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("Online")


@bot.event
async def on_member_join (member):

        await member.create_dm()
        await member.dm_channel.send (f'Hi {member.name}, welcome to my Discord server!')



@bot.event
async def on_message(message):
    Stringo = message.content
    try:
        if Stringo[0:2] == '!!':
            if Stringo == "!!syntax" or Stringo == "!!help": #!!help command or !!syntax, shows the commands
                help_msg = "Implemented commands: !!search, !!page, !!random, !!image, !!categories, !!link, !!reference, !!section, !!suggest, !!content, !!summary"
                await message.channel.send(help_msg)
            elif message.content.startswith("!!search"): #searches about a specific topic
                search = Stringo[8:]
                result = wikipedia.search(search, 20)
                await message.channel.send(result)

            elif message.content.startswith("!!page"): #searches for a specific page
                search = Stringo[6:]
                try:
                    result = wikipedia.page(search, preload=True)
                    await message.channel.send(result)
                except wikipedia.exceptions.PageError:
                    await message.channel.send("Page not found")

            elif message.content.startswith("!!random"): #returns a random page
                tempo = wikipedia.random(pages = 1)
                result = wikipedia.summary(tempo, 4)
                await message.channel.send(result)

            elif message.content.startswith("!!image"): #returns an image about the topic
                search = Stringo[7:]
                WikipediaClass = wikipedia.WikipediaPage(search)
                result = WikipediaClass.images
                await message.channel.send(result)

            elif message.content.startswith("!!categories"): #returns the categories about the topic
                search = Stringo[11:]
                try:
                    WikipediaClass = wikipedia.WikipediaPage(search)

                    result = WikipediaClass.categories
                except:
                    await message.channel.send('Not found')
                else:
                    await message.channel.send(result)

            elif message.content.startswith("!!link"): #returns the link about a topic
                search = Stringo[6:]
                WikipediaClass = wikipedia.WikipediaPage(search, preload=True)
                tempo = WikipediaClass.links
                result = ""
                for i in tempo:
                    if len(result) <= 1960:
                        result += i
                        result += ", "
                    else:
                        break


                await message.channel.send(result[:1999])

            elif message.content.startswith("!!reference"): #return the refrences about a topic
                search = Stringo[10:]
                try:
                    WikipediaClass = wikipedia.WikipediaPage(search)
                    result = WikipediaClass.references
                except:
                    await message.channel.send("Not found")
                else:
                    await message.channel.send(result)

            elif message.content.startswith("!!section"): #return the sections about a topic
                search = Stringo[9: ]
                WikipediaClass = wikipedia.WikipediaPage(search)
                result = WikipediaClass.sections
                await message.channel.send(result)

            elif message.content.startswith("!!suggest"): #return the suggested topic
                search = Stringo[9:]
                result = wikipedia.suggest(search)
                try:
                    await message.channel.send(result)
                except:
                    await message.channel.send("Not valid")
            elif message.content.startswith("!!content"): #returns what is included in that page, regarding the topic
                search = Stringo[9:]
                try:
                    WikipediaClass = wikipedia.WikipediaPage(search)
                    result = WikipediaClass.content

                    await message.channel.send(result[0:1999])
                except:
                    await message.channel.send("Not valid")

            elif message.content.startswith("!!summary"): #returns a summary, if num provided, it will be established with the user, else, num = 4, returns a summary about the topic.
                 try:
                      num = int(Stringo[-1])
                 except ValueError:
                     num = 4
                 finally:
                      search = Stringo[9:]
                      result = wikipedia.summary(search, num)
                      await message.channel.send(result)
            elif message.content.startswith("!!sum"):
                 try:
                      num = int(Stringo[-1])
                 except ValueError:
                     num = 4
                 finally:
                      search = Stringo[5:]
                      result = wikipedia.summary(search, num)
                      await message.channel.send(result[0:1999])

            else:
                await message.channel.send("Not valid")
    except:
        await message.channel.send("An unknown error occured, please report the it to @Uy Scuti#3533")



bot.run(TOKEN)
