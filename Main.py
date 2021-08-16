import discord

from discord.ext.commands import Bot

import json

from Wikipedia import *

from Math import *

from MorseCode import *

from Reminders import *

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


def FindTheIntegers(List):
    x = ""
    for i in List:
        try:
            int(i)
            x += i
        except:
            pass
    return int(x)


Bot = Bot(command_prefix='~')  # sets the prefix

@Bot.event
async def on_ready():
    await Bot.change_presence(status=discord.Status.online, activity=discord.Game("Waiting to help you"))
    print("Online")


@Bot.event  # message function
async def on_message(message):
    Message = str(message.content)
    if Message[0:10] == "~wikipedia":
        WordStep1 = Message.split(" ")
        Word = WordStep1[2:]
        Word = " ".join(Word)
        Language = ReturnLanguage(message.guild)
        if Message[0:18] == "~wikipedia summary":
            Result = Summary(Word, Language)
            await message.channel.send(Result)

        elif Message[0:17] == "~wikipedia search":
            Result = search(Word, Language)
            await message.channel.send(Result)

        elif Message[0:20] == "~wikipedia reference":
            Result = reference(Word, Language)
            await message.channel.send(Result)

        elif Message[0:17] == "~wikipedia random":
            Result = Random(Language)
            await message.channel.send(Result)

        elif Message[0:16] == "~wikipedia image":
            Result = Images(Word)
            await message.channel.send(Result)

        elif Message[0:21] == "~wikipedia categories":
            Result = Categories(Word, Language)
            await message.channel.send(Result)

        elif Message[0:15] == "~wikipedia link":
            Result = Link(Word, Language)
            await message.channel.send(Result)

        elif Message[0:15] == "~wikipedia test":
            Result = Test(Word, Language)
            await message.channel.send(Result)

        elif Message[0:18] == "~wikipedia section":
            Result = Section(Word, Language)
            await message.channel.send(Result)

        elif Message[0:14] == "~wikipedia url":
            Result = url(Word, Language)
            await message.channel.send(Result)

        elif Message[0:17] == "~wikipedia simple":
            Result = Simple(Word, Language)
            await message.channel.send(Result)

        else:
            await message.channel.send("Invalid Command")



    elif Message[0:5] == "~math":
        if Message[0:15] == "~math solveforx":
            Equation = Message[16:]
            if '=' not in Equation:
                await message.channel.send("Not equal to a value")
            else:
                if Equation.count("=") > 1:
                    await message.channel.send("More than 1 equal signs, inequalities if this is the case are not included")
                else:
                    Answer = Equation[(Equation.index('=')+1):]
                    Equationwithoutanswer = Equation[:Equation.index("=")]
                    Expression = sympify(Equationwithoutanswer)
                    Answer = sympify(Answer)
                    Answer = SolveForX(Expression, Answer)
                    await message.channel.send(Answer)

        elif Message[0:10] == "~math sind":
            value = Message[11:]
            try:
                value = float(value)
            except:
                await message.channel.send("Not a real value")
            else:
                await message.channel.send(SinD(value))

        elif Message[0:10] == "~math sinr":
            value = Message[11:]
            try:
                value = float(value)
            except:
                await message.channel.send("Not a real value")
            else:
                await message.channel.send(SinR(value))

        elif Message[0:10] == "~math cosd":
            value = Message[11:]
            try:
                value = float(value)
            except:
                await message.channel.send("Not a real value")
            else:
                await message.channel.send(CosD(value))

        elif Message[0:10] == "~math cosr":
            value = Message[11:]
            try:
                value = float(value)
            except:
                await message.channel.send("Not a real value")
            else:
                await message.channel.send(CosR(value))

        elif Message[0:10] == "~math tand":
            value = Message[11:]
            try:
                value = float(value)
            except:
                await message.channel.send("Not a real value")
            else:
                await message.channel.send(TanD(value))

        elif Message[0:10] == "~math tanr":
            value = Message[11:]
            try:
                value = float(value)
            except:
                await message.channel.send("Not a real value")
            else:
                await message.channel.send(TanR(value))

        elif Message[0:13] == "~math arcsind":
            value = Message[14:]
            try:
                value = float(value)
            except:
                await message.channel.send("Not a real value")
            else:
                await message.channel.send(ArcSinD(value))

        elif Message[0:13] == "~math arcsinr":
            value = Message[14:]
            try:
                value = float(value)
            except:
                await message.channel.send("Not a real value")
            else:
                await message.channel.send(ArcSinR(value))

        elif Message[0:13] == "~math arccosd":
            value = Message[14:]
            try:
                value = float(value)
            except:
                await message.channel.send("Not a real value")
            else:
                await message.channel.send(ArcCosD(value))

        elif Message[0:13] == "~math arccosr":
            value = Message[14:]
            try:
                value = float(value)
            except:
                await message.channel.send("Not a real value")
            else:
                await message.channel.send(ArcCosR(value))

        elif Message[0:13] == "~math arctand":
            value = Message[14:]
            try:
                value = float(value)
            except:
                await message.channel.send("Not a real value")
            else:
                await message.channel.send(ArcTanD(value))

        elif Message[0:13] == "~math arctanr":
            value = Message[14:]
            try:
                value = float(value)
            except:
                await message.channel.send("Not a real value")
            else:
                await message.channel.send(ArcTanR(value))

        elif Message[0:15] == "~math toradians":
            value = Message[16:]
            try:
                value = float(value)
                await message.channel.send(ToRadians(value))
            except:
                await message.channel.send("Invalid value")

        elif Message[0:15] == "~math todegrees":
            value = Message[16:]
            try:
                value = float(value)
                await message.channel.send(ToDegrees(value))
            except:
                await message.channel.send("Invalid value")

        elif Message[0:15] == "~math remainder":
            value = Message[16:]
            if '/' not in value:
                await message.channel.send("no '/' in the expression")
            else:
                Number = value[:value.index("/")]
                Divided = value[value.index('/') +1:]
                await message.channel.send(Remainder(Number, Divided))

        elif Message[0:17] == "~math eucdistance":

            Value = Message.split(" ")[-1]
            Point1 = Value.split("_")[0]
            Point2 = Value.split("_")[1]

            x1 = FindTheIntegers(Point1.split(",")[0])
            y1 = FindTheIntegers(Point1.split(",")[1])
            x2 = FindTheIntegers(Point2.split(",")[0])
            y2 = FindTheIntegers(Point2.split(",")[1])

            Value = EucDistance((x1,y1), (x2,y2))
            await message.channel.send(Value)

        elif Message[0:8] == "~math pi":
            await message.channel.send(Pi())

        elif Message[0:7] == "~math e":
            await message.channel.send(e())

        elif Message[0:9] == "~math tau":
            await message.channel.send(Tau())

        elif Message[0:8] == "~math ln":
            Value = Message[9:]
            try:
                Value = ln(float(Value))
            except:
                await message.channel.send("Not an integer nor a float")
            await message.channel.send(Value)

        elif Message[0:9] == "~math log":
            Value = Message[10:]
            Base = Value.split(",")[0]
            Exponent = Value.split(",")[1]
            Base = FindTheIntegers(Base)
            Exponent = FindTheIntegers(Exponent)
            Value = log(Exponent, Base)
            await message.channel.send(Value)

        elif Message[0:10] == "~math sqrt":
            Value = Message[11:]
            Value = FindTheIntegers(Value)
            Value = sqrt(Value)
            await message.channel.send(Value)

        elif Message[0:9] == "~math pow":
            Value = Message[10:]
            Base = FindTheIntegers(Value.split(',')[0])
            Exponent = FindTheIntegers(Value.split(',')[1])
            Value = pow(Base, Exponent)
            await message.channel.send(Value)

        elif Message[0:21] == "~math differentiation":
            await message.channel.send("Function under development")
        elif Message[0:11] == "~math limit":
            await message.channel.send("Function under development")
        else:
            await message.channel.send("Invalid command")

    elif Message[:6] == ("~morse"):
        if Message[:13] == "~morse encode":
            EncodeMessage = Message[14:]
            EncodeMessage = MorseEncoder(EncodeMessage)
            await message.channel.send(EncodeMessage)

        elif Message[:13] == "~morse decode":
            DecodeMessdage = Message[14:]
            DecodeMessdage = MorseDecoder(DecodeMessdage)
            await message.channel.send(DecodeMessdage)

    elif Message[:9] == "~reminder":
        if Message[:13] == "~reminder get":
            Reminder = GetReminders(message.author)
            await message.channel.send(Reminder)

        elif Message[:13] == "~reminder set":
            Reminder = Message[14:]
            try:
                SetReminders(message.author, Reminder)
                await message.channel.send("Done")
            except:
                await message.channel.send("An unknown error occurred, please try again later")

        elif Message[:13] == "~reminder del":
            Reminder = Message[14:]
            Result = DeleteReminder(message.name, Reminder)
            if Result == False:
                await message.channel.send("No Reminder exists by that name")
            else:
                await message.channel.send("Done")

    elif Message[:9] == "~settings":
        Unit = Message[10:]
        Unit = Unit.lower()
        if Unit == "math":
            Functions = ['SolveForX {equation}', 'SinD {value}', 'SinR {Value}', 'CosD {Value}', 'CosR {Value}', 'TanD {Value}', 'TanR {Value}', 'ArcSinD {Value}', 'ArcSinR {Value}', 'ArcCosD {Value}','ArcCosR {Value}', \
                         'ArcTanD {Value}', 'ArcTanR {Value}', 'ToRadians {Value}', 'ToDegrees {Value}', 'Reminder ({dividend}, {divisor})', 'EucDistance ({x1}, {x2})_({x2},{y2})', 'pi', 'e', 'tau', 'ln {Value}', \
                         'log ({Base}, {Value})', 'sqrt {Value}',  'pow ({Base}, {Exponent}'
                        ]
        elif Unit == "reminder":
            pass
        elif Unit == "morse":
            pass
        elif Unit == "wikipedia":
            pass
        else:
            message.channel.send("No Unit by that name is found")



Bot.run("ODQ4NDc0OTA5MTU0NzM4MjA2.YLNJ1g.tdzcgXxlLGWG7bSqVXK5Ic3TTUA")
