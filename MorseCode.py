def MorseEncoder(Message):
    """
    :param Message: The message that wants to be changed into morse code
    :return: returns a string with morse code
    """
    EncoderValues = {
               'a':'. -',
               'b':'- . . .',
               'c':'- . - .',
               'd':'- . .',
               'e':'.',
               'f':'. . - .',
               'g':'- - .',
               'h':'. . . .',
               'i':'. .',
               'j':'. - - -',
               'k':'- . -',
               'l':'. - . .',
               'm':'- -',
               'n':'- .',
               'o':'- - -',
               'p':'. - - .',
               'q':'- - . -',
               'r':'. - .',
               's':'. . .',
               't':'-',
               'u':'. . -',
               'v':'. . . -',
               'w':'. - -',
               'x':'- . . -',
               'y':'- . - -',
               'z':'- - . .',
               '1':'. - - - -',
               '2':'. . - - -',
               '3':'. . . - -',
               '4':'. . . . -',
               '5':'. . . . .',
               '6':'- . . . .',
               '7':'- - . . .',
               '8':'- - - . .',
               '9':'- - - - .',
               '0':'- - - - -'}

    Message = Message.lower()

    NewMessage = ""
    for i in Message:
        if i == " ":
            NewMessage += "||"
        else:
            Value = EncoderValues.get(i)
            if Value == None:
                return "Message cannot be encoded due to random letters"
            else:
                NewMessage += Value
                NewMessage += "__"
    return NewMessage

def MorseDecoder(Message):
    """
    :param Message:
    :return:
    """
    Decode = {'. -': 'a',
     '- . . .': 'b',
     '- . - .': 'c',
     '- . .': 'd',
     '.': 'e',
     '. . - .': 'f',
     '- - .': 'g',
     '. . . .': 'h',
     '. .': 'i',
     '. - - -': 'j',
     '- . -': 'k',
     '. - . .': 'l',
     '- -': 'm',
     '- .': 'n',
     '- - -': 'o',
     '. - - .': 'p',
     '- - . -': 'q',
     '. - .': 'r',
     '. . .': 's',
     '-': 't',
     '. . -': 'u',
     '. . . -': 'v',
     '. - -': 'w',
     '- . . -': 'x',
     '- . - -': 'y',
     '- - . .': 'z',
     '. - - - -': '1',
     '. . - - -': '2',
     '. . . - -': '3',
     '. . . . -': '4',
     '. . . . .': '5',
     '- . . . .': '6',
     '- - . . .': '7',
     '- - - . .': '8',
     '- - - - .': '9',
     '- - - - -': '0'}

    Words = Message.split("||")
    letters = []
    for i in Words:
        letters.append(i.split("__"))
    Sentence = ""
    for i in letters:
        Word = ""
        for j in i[:len(i)-1]:
            x = Decode.get(j)
            if x == None:
                return "There are letters that arent there"
            else:
                Word += x
        Sentence += Word
        Sentence += " "
    return Sentence


