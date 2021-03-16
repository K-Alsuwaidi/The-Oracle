import discord

from discord.ext.commands import Bot

import wikipedia
import wikipediaapi
#import modules
WikiClass = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI) #initiates teh wikipedia class

Bot = Bot(command_prefix = '~') #sets the prefix


@Bot.event  #on ready function
async def on_ready():
    game = discord.Game("Browing Wikipedia, Prefix: ~")
    await Bot.change_presence(status=discord.Status.online, activity=game) #sets the status
    print("Online") #shows that the bot is online

@Bot.event #message function
async def on_message(message):
    Stringo = message.content
    if Stringo[0:1] == '~':
        if message.content.startswith("~help"):
            await message.channel.send("Implement commands: ~help, ~summary, ~search, ~reference, ~random, ~image, ~categories, ~link, ~test, ~page, ~content, ~section, ~sum, and ~url")

        elif message.content.startswith("~summary"):
            search = Stringo[9:] #gets the search
            page = WikiClass.page(search) #makes the page
            result = page.summary[:500] #gets the summary len 200 chars
            ListSplited = result.split(".") #spltis the summary to get sentences
            x = 0
            StringResult = ""
            for i in ListSplited: #for loop to add 5 sentences to the result
                StringResult += i
                if x == 5:
                    break
                x+= 1
            await message.channel.send(StringResult) #sends result

        elif message.content.startswith("~search"):
                search = Stringo[8:] #gets the search
                result = wikipedia.search(search, 20) #searches for the topics that are connected with the search
                await message.channel.send(result) #sends result


        elif message.content.startswith("~reference"):
            search = Stringo[11:]
            try:
                WikipediaClass = wikipedia.WikipediaPage(search)
                result = WikipediaClass.references
            except:
                await message.channel.send("Not found")
            else:
                SendResult = result[0:5]
                await message.channel.send(tuple(SendResult))



        elif message.content.startswith("~random"):
            search = wikipedia.random(pages = 1) #searches for a random page
            page = WikiClass.page(search) #makes the page
            result = page.summary[:1000] #gets the summary len 200 chars
            ListSplited = result.split(".") #spltis the summary to get sentences
            x = 0
            StringResult = ""
            for i in ListSplited: #for loop to add 5 sentences to the result
                StringResult += i
                if x == 5:
                    break
                x+= 1
            await message.channel.send(StringResult) #sends result


        elif message.content.startswith("~image"):
            search = Stringo[7:] #search
            WikipediaClass = wikipedia.WikipediaPage(search) #makes the wikipedia class
            result = WikipediaClass.images #gets the images
            for i in result[:len(result)//2]: #loops over the list
                await message.channel.send(i) #sends the images


        elif message.content.startswith("~categories"):
            search = Stringo[12:] #search
            try: #if an error arises or the page doesnt exist
                WikipediaClass = wikipedia.WikipediaPage(search) # makes the wikipedia class

                result = WikipediaClass.categories #gets the categories
            except: #if error arise
                await message.channel.send('Page not found') #sends that page not found
            else:
                await message.channel.send(result) #send the result


        elif message.content.startswith("~link"):
            search = Stringo[6:]
            try: #try if an error arises
                WikipediaClass = wikipedia.page(search) #makes the class
                result = WikipediaClass.url #gets the url
                await message.channel.send(result) #sends the result
            except Exception as e:
                print(e)
                await message.channel.send("Page not found") #if error pops up, transfers to this


        elif message.content.startswith("~test"):
            search = Stringo[6:]   #search
            page = WikiClass.page(search) #makes the class
            if page.exists(): #checks
                await message.channel.send("Page exists") #if true print it exists
            else: #else
                await message.channel.send("Page doesnt exist") #print it does not exist


        elif message.content.startswith("~page"):
            search = Stringo[6:] #search
            page = WikiClass.page(search) #class page
            result = page.text #gets result
            if len(result) <=2000: #if its acceptable with discord
                await message.channel.send(result) #sends it if true
            else: #else
                for i in range(len(result)//2000): #for loop, divides the result by 2000 to get an integer, a value, if 10000 = 5 and so on
                    await message.channel.send(result[2000*i:2000*(i+1)]) #for loop and sends the text 2000 per time,

        elif message.content.startswith("~content"):
            search = Stringo[9:] #search
            page = WikiClass.page(search) #class page
            result = page.text #gets result
            if len(result) <=2000: #if its acceptable with discord
                await message.channel.send(result) #sends it if true
            else: #else
                for i in range(len(result)//2000): #for loop, divides the result by 2000 to get an integer, a value, if 10000 = 5 and so on
                    await message.channel.send(result[2000*i:2000*(i+1)]) #for loop and sends the text 2000 per time,


        elif message.content.startswith("~section"):
            search = Stringo[9:] #search
            page = WikiClass.page(search)
            result = page.sections
            StringReturned = ""
            for i in result:
                StringReturned += i.title #adds title
                StringReturned += ": " #adds :
                StringReturned += i.text[0:40] #adds text 40 chars
                StringReturned += ", " #adds comma
            await message.channel.send(StringReturned) #send msg

        elif message.content.startswith("~sum"):
            search = Stringo[5:] #gets the search
            page = WikiClass.page(search) #makes the page class
            result = page.summary[:500] #gets the summary len 200 chars
            ListSplited = result.split(".") #spltis the summary to get sentences
            x = 0
            StringResult = ""
            for i in ListSplited: #for loop to add 5 sentences to the result
                StringResult += i
                if x == 5:
                    break
                x += 1
            await message.channel.send(StringResult) #sends result


        elif message.content.startswith("~url"):
            search = Stringo[5:] #search
            page = WikiClass.page(search) #makes the page class
            result = page.fullurl #gets full url
            await message.channel.send(result) #sends result
        else:
            await message.channel.send("Unknown refrence, please write ~help for more options, if you have a suggestion dm @Uy Scuti#3533 in discord") #if command doesnt match any of the above



Bot.run(TOKEN)
