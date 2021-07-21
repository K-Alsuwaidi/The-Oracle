import discord

from discord.ext.commands import Bot

import wikipedia

import wikipediaapi

import json

import googlesearch

from urllib.request import urlopen

from bs4 import BeautifulSoup

# import modules

with open("TOKEN.txt", 'r') as f:
    TOKEN = f.readline()
    f.close()


def ReturnLanguage(guild):
    "returns the server's language"
    with open("server_languages.json", "r") as f:  # opens the file
        dicto = json.load(f)  # loads the dictionary
        f.close()  # closes the file

    if dicto.get(guild) != None:
        return dicto.get(guild)
    return "en"


CurrentStatus = []
WikiClass = wikipediaapi.Wikipedia(language='en',
                                   extract_format=wikipediaapi.ExtractFormat.WIKI)  # initiates the wikipedia class
Bot = Bot(command_prefix='~')  # sets the prefix
NumberOfMessages = []


@Bot.event  # on ready function
async def on_ready():
    CurrentStatus.append("Browing Wikipedia")
    await Bot.change_presence(status=discord.Status.online, activity=discord.Game(CurrentStatus[0]))
    print("Online")  # shows that the bot is online


@Bot.event  # message function
async def on_message(message):
    Stringo = message.content
    Stringo = Stringo.lower()
    languag = "en"  # sets temp language
    wikipedia.set_lang('en')  # sets temp language
    if Stringo[0:1] == '~':  # checks if its a command or normal msg
        NumberOfMessages.append('.')
        if len(NumberOfMessages) == 5:
            for i in range(5):
                NumberOfMessages.pop(0)
            if CurrentStatus[0] == ("Browing Wikipedia"):
                CurrentStatus[0] = ("Prefix: ~")
            else:
                CurrentStatus[0] = ("Browing Wikipedia")
            await Bot.change_presence(status=discord.Status.online, activity=discord.Game(CurrentStatus[0]))

        if message.content.startswith("~help"):  # if command == ~help
            await message.channel.send(
                "Implement commands: ~help, ~summary, ~search, ~reference, ~random, ~image, ~categories, ~link, ~test, ~page, ~content, ~section, ~sum, ~settings, ~simple, and ~url")  # sends the commands



        elif message.content.startswith("~summary"):  # if it starts with ~summary

            search = Stringo[9:]  # gets the search

            m = str(message.guild)  # sets the guild as m, type == str

            Languag = ReturnLanguage(guild)

            WikiClass = wikipediaapi.Wikipedia(language=languag,
                                               extract_format=wikipediaapi.ExtractFormat.WIKI)  # initiates the wikipedia class and sets the language depending on the server choice

            page = WikiClass.page(search)  # makes the page
            result = page.summary[:500]  # gets the summary len 500 chars

            ListSplited = result.split(".")  # splits the summary to get sentences
            x = 0  # sets the itterative value as 0
            StringResult = ""  # new string for the 5 sentences

            for i in ListSplited:  # for loop to add 5 sentences to the result
                StringResult += i  # adds i to StringResult, i = value from ListSplited
                if x == 5:  # if there are 5 sentences
                    StringResult += "."  # adds a fullstop to the last sentence
                    break  # breaks out of loop
                x += 1  # adds 1 if the value is less than 5, less than 5 sentences

            try:  # check if there is an error
                await message.channel.send(StringResult)  # sends result

            except discord.errors.HTTPException:  # None Error, or discord error

                wikipedia.set_lang(languag)  # sets the language, using wikipedia library
                result = wikipedia.summary(search, sentences=5)  # fetches the summary, number of sentences is 5

                try:  # try if the summary didnt return none
                    await message.channel.send(result)  # sends result
                except:  # An error arises with it trying to send a result, most probably None error as it was checked with 2 libraries
                    await message.channel.send("Page not found")  # Informs the user that no page has matched the query



        elif message.content.startswith("~search"):  # if its equal to ~search



            guild = str(message.guild)  # sets the guild as m, type == str

            Languag = ReturnLanguage(guild)


            wikipedia.set_lang(languag)  # assigns the value

            search = Stringo[8:]  # gets the search
            result = wikipedia.search(search, 20)  # searches for the topics that are connected with the search

            try:
                await message.channel.send(result)  # sends result
            except:  # an error arose
                await message.channel.send("No page has been found")  # sends the msg



        elif message.content.startswith("~reference"):  # if it matches reference


            guild = str(message.guild)  # sets the guild as m, type = str

            Languag = ReturnLanguage(guild)

            wikipedia.set_lang(languag)  # assigns the value

            search = Stringo[11:]  # assign the search value

            try:
                WikipediaClass = wikipedia.WikipediaPage(search)  # makes the class
                result = WikipediaClass.references  # gets the refernces

            except:  # if an error arises with the code up
                await message.channel.send("Not found")  # sends this msg

            else:  # if no error arose
                SendResult = result[0:5]  # sets the first 5 references

                try:
                    listo = list(SendResult)  # makes the result as a list
                    if len(listo) == 0:  # if the list is empty
                        await message.channel.send("No reference has been found")  # sends this msg
                    else:  # if listo is not empty
                        await message.channel.send(listo)  # sends the listo

                except discord.errors.HTTPException:  # File == None
                    await message.channel.send("Page not found")  # Sends this msg



        elif message.content.startswith("~random"):  # if msg == ~random


            guild = str(message.guild)  # sets the guild as guild, type = str

            Languag = ReturnLanguage(guild)


            WikiClass = wikipediaapi.Wikipedia(language=languag,
                                               extract_format=wikipediaapi.ExtractFormat.WIKI)  # initiates the wikipedia class

            search = wikipedia.random(pages=1)  # searches for a random page
            page = WikiClass.page(search)  # makes the page

            result = page.summary[:1000]  # gets the summary len 200 chars
            ListSplited = result.split(".")  # spltis the summary to get sentences
            x = 0
            StringResult = ""

            for i in ListSplited:  # for loop to add 5 sentences to the result
                StringResult += i  # adds an element from ListSplited to StringResult
                if x == 5:  # checks if there are 5 sentences
                    StringResult += "."  # adds a full stop to the last sentence
                    break  # breaks out of the loop
                x += 1  # if less than 5 sentences, adds 1 to x

            await message.channel.send(StringResult)  # sends result



        elif message.content.startswith("~image"):  # if msg == ~image

            search = Stringo[7:]  # search

            WikipediaClass = wikipedia.WikipediaPage(search)  # makes the wikipedia class
            result = WikipediaClass.images  # gets the images

            x = 0
            for i in result:  # loops over the list
                await message.channel.send(i)  # sends the images
                if x == 5:
                    break
                else:
                    x += 5


        elif message.content.startswith("~categories"):  # if msg == ~categories

            search = Stringo[12:len(Stringo) - 1]  # search


            guild = str(message.guild)  # sets the guild as guild, type = str

            Languag = ReturnLanguage(guild)

            wikipedia.set_lang(languag)  # assigns the value

            WikipediaClass = wikipedia.page(search)  # makes the class
            result = WikipediaClass.categories  # gets the categories
            print(len(result))
            print(type(result))
            print(result)

            try:
                await message.channel.send(result[0:10])  # send the result
            except:
                await message.channel.send("Page not found")



        elif message.content.startswith("~link"):  # if user requests link to the website


            guild = str(message.guild)  # sets the guild as m, type = str

            Languag = ReturnLanguage(guild)

            wikipedia.set_lang(languag)  # assigns the value

            search = Stringo[6:len(Stringo) - 1]  # gets the search

            try:  # try if an error arises
                WikipediaClass = wikipedia.page(search)  # makes the class
                result = WikipediaClass.url  # gets the url
                await message.channel.send(result)  # sends the result

            except Exception as e:
                print(e)
                await message.channel.send("Page not found")  # if error pops up, transfers to this


        elif message.content.startswith("~test"):  # if the user want to see if the page exist

            search = Stringo[6:]  # search

            Languag = ReturnLanguage(guild)

            WikiClass = wikipediaapi.Wikipedia(language=Languag,
                                               extract_format=wikipediaapi.ExtractFormat.WIKI)  # initiates the wikipedia class
            page = WikiClass.page(search)  # makes the class

            if page.exists():  # checks
                await message.channel.send("Page exists")  # if true print it exists

            else:  # else
                await message.channel.send("Page doesnt exist")  # print it does not exist


        elif message.content.startswith("~page"):  # if the user want the page


            guild = str(message.guild)  # sets the guild as m, type = str

            Languag = ReturnLanguage(guild)

            WikiClass = wikipediaapi.Wikipedia(language=languag,
                                               extract_format=wikipediaapi.ExtractFormat.WIKI)  # initiates the wikipedia class

            search = Stringo[6:]  # search
            page = WikiClass.page(search)  # class page
            result = page.text  # gets result

            if len(result) <= 2000:  # if its acceptable with discord
                await message.channel.send(result)  # sends it if true

            else:  # else

                for i in range(len(
                        result) // 2000):  # for loop, divides the result by 2000 to get an integer, a value, if 10000 = 5 and so on
                    await message.channel.send(
                        result[2000 * i:2000 * (i + 1)])  # for loop and sends the text 2000 per time,

        elif message.content.startswith("~content"):


            guild = str(message.guild)  # sets the guild as m, type = str

            Languag = ReturnLanguage(guild)

            WikiClass = wikipediaapi.Wikipedia(language=languag,
                                               extract_format=wikipediaapi.ExtractFormat.WIKI)  # initiates the wikipedia class

            search = Stringo[9:]  # search

            page = WikiClass.page(search)  # class page
            result = page.text  # gets result

            if len(result) <= 2000:  # if its acceptable with discord
                await message.channel.send(result)  # sends it if true
            else:  # else

                for i in range(len(
                        result) // 2000):  # for loop, divides the result by 2000 to get an integer, a value, if 10000 = 5 and so on
                    await message.channel.send(
                        result[2000 * i:2000 * (i + 1)])  # for loop and sends the text 2000 per time,


        elif message.content.startswith("~section"):  # if msg == ~section


            guild = str(message.guild)  # sets the guild as m, type = str

            Languag = ReturnLanguage(guild)

            WikiClass = wikipediaapi.Wikipedia(language=languag,
                                               extract_format=wikipediaapi.ExtractFormat.WIKI)  # initiates the wikipedia class

            search = Stringo[9:]  # search

            page = WikiClass.page(search)  # gets the page
            result = page.sections  # gets the sections

            for i in result:  # the result
                StringReturned = ""  # resets StringReturned
                StringReturned += i.title  # adds title
                StringReturned += ": "  # adds :
                StringReturned += i.text[0:40]  # adds text 40 chars
                await message.channel.send(StringReturned)  # sends msg and loops

        elif message.content.startswith("~sum"):  # if it starts with ~summary

            search = Stringo[5:]  # gets the search

            guild = str(message.guild)  # sets the guild as m, type == str

            Languag = ReturnLanguage(guild)

            WikiClass = wikipediaapi.Wikipedia(language=languag,
                                               extract_format=wikipediaapi.ExtractFormat.WIKI)  # initiates the wikipedia class and sets the language depending on the server choice

            page = WikiClass.page(search)  # makes the page
            result = page.summary[:500]  # gets the summary len 500 chars

            ListSplited = result.split(".")  # splits the summary to get sentences
            x = 0  # sets the itterative value as 0
            StringResult = ""  # new string for the 5 sentences

            for i in ListSplited:  # for loop to add 5 sentences to the result
                StringResult += i  # adds i to StringResult, i = value from ListSplited
                if x == 5:  # if there are 5 sentences
                    StringResult += "."  # adds a fullstop to the last sentence
                    break  # breaks out of loop
                x += 1  # adds 1 if the value is less than 5, less than 5 sentences

            try:  # check if there is an error
                await message.channel.send(StringResult)  # sends result

            except discord.errors.HTTPException:  # None Error, or discord error

                wikipedia.set_lang(languag)  # sets the language, using wikipedia library
                result = wikipedia.summary(search, sentences=5)  # fetches the summary, number of sentences is 5

                try:  # try if the summary didnt return none

                    await message.channel.send(result)  # sends result


                except:  # An error arises with it trying to send a result, most probably None error as it was checked with 2 libraries
                    await message.channel.send("Page not found")  # Informs the user that no page has matched the query





        elif message.content.startswith("~url"):  # if msg  == ~url

            search = Stringo[5:]  # search

            guild = str(message.guild)  # sets the guild as m, type == str

            Languag = ReturnLanguage(guild)

            wikipedia.set_lang(languag)  # assigns the value

            page = WikiClass.page(search)  # makes the page class
            result = page.fullurl  # gets full url

            await message.channel.send(result)  # sends result



        elif message.content.startswith("~settings"):  # if msg == ~settings

            if len(Stringo) == 9:  # checks if the user just requested the settings
                await message.channel.send(
                    "Set server's language with '~settings {}', The languages are: English = en, Swedish = sv, German = de, French = fr, Dutch = nl, Russian = ru, Italian, = it, Spanis = es, Polish = pl, Japanese = ja, and Arabic = ar.")  # sends this msg

            else:

                Languages = ["en", "ceb", "sv", "de", "fr", 'nl', "ru", "it", "es", "pl", "ja",
                             "ar"]  # sets the languages

                for i in Languages:  # loop over the languages above to check that the user input is the right value
                    if Stringo[10:] == i:  # if it was found

                        with open("server_languages.json", "r") as f:  # opens the json file, read, as f
                            dicto = json.load(f)  # loads dicto
                            f.close()  # closes the file

                        with open("server_languages.json", "w") as f:  # opens the file, write, as f
                            m = str(message.guild)  # gets the guild as m, type == str

                            dicto[m] = Stringo[10:]  # adds it to the dicto

                            json.dump(dicto, f, indent=4)  # dump the dicto to the json file with an indent of 4

                            Msg = "Language set: "  # add this msg to Msg
                            Msg += str(Stringo[10:])  # adds the language chosen
                            Msg += " for "  # adds this msg to Msg
                            Msg += m  # adds the server name

                            await message.channel.send(Msg)  # sends msg
                            f.close()  # closes the file


        elif message.content.startswith("~simple"):  # if msg == ~simple

            with open("server_languages.json", "r") as f:  # opens the file
                dicto = json.load(f)  # loads the dictionary
                f.close()  # closes the file

            m = str(message.guild)  # sets the guild as m, type = str

            if dicto.get(m) != None:  # checks if the user has set a language for the server
                for i in dicto.keys():  # checks the dicto keys
                    if i == m:  # if the key matches the server name
                        if dicto[i] != "en":
                            await message.channel.send(
                                "Only works with english")  # sends this msg if its not in english

                        else:
                            search1 = Stringo[8:]  # finds the search
                            search2 = "https://simple.wikipedia.org/wiki/" + search1  # adds it to the url
                            gsearch = googlesearch.search(search2)  # searches the url

                            for j in gsearch:  # finds the search
                                link = j  # assign it to link
                                break  # break out of the loop

                            break  # break out of the other loop

            source = urlopen(search2).read()  # reads the url
            soup = BeautifulSoup(source, "html.parser")  # uses html.parser
            text = ""  # makes the text file
            for paragraph in soup.find_all('p'):  # a for loop for the text under p
                text += paragraph.text  # adds the text to the variable

            ListSplited = text.split(".")  # splits the text
            x = 0  # makes x
            StringResult = ""  # for loop variable add
            for i in ListSplited:  # makes the foor loop
                StringResult += i  # adds the value from ListSplited to StringResult
                if x == 5:  # if x == 5
                    StringResult += "."  # adds a fullstop to the last sentence
                    break  # breaks
                x += 1  # x less than 5, adds 1 to the value x
            Returned = StringResult + " Link: " + str(link)  # adds the return values to 1 string

            try:  # try
                await message.channel.send(Returned)  # sends the link
            except:  # if an error arose with the send function
                await message.channel.send("Not found")  # sends this msg

        else:
            await message.channel.send(
                "Unknown reference, please write ~help for more options, if you have a suggestion dm @Uy Scuti#3533 in discord")  # if command doesnt match any of the above


Bot.run(TOKEN)
