from urllib.request import urlopen

from bs4 import BeautifulSoup

import wikipedia

import wikipediaapi



def Summary(Search, Language):
    """
    :param Search: Search
    :param Language: Language set by the user
    :return: Summary of the given title, if not found, tries to write it directly in the url, if not found, sends error message
    """
    WikiClass = wikipediaapi.Wikipedia(language=Language, extract_format=wikipediaapi.ExtractFormat.WIKI)  # initiates the wikipedia class and sets the language depending on the server choice
    page = WikiClass.page(Search) #sets the page
    result = page.summary[0:2000] #gets the summary
    NumOfSentences = 0 #sets Number of sentences to 0
    if len(result) != 0: # checks that the result isn't empty
        ListSplited = result.split(".") #sets each element as a sentence in a list
        StringResult = "" #sets the String result

        if len(ListSplited) <= 5: #if it is than 5 sentences, gets more characters
            result = page.summary[0:3000]
            ListSplited = result.split(".") #splits the new characters
        else:
            for i in ListSplited: #loops around the list of sentences and gets 5 sentences
                StringResult += i
                if NumOfSentences == 5:
                    StringResult+="."
                    break
                NumOfSentences += 1
            return StringResult #returns
    else:
        try:
            StringResult = wikipedia.summary(Search, sentences = 5) #checks using other api if the web is open if not error arise
            return StringResult
        except: #checks if language is en, then uses bs4 and urlopen to open the html page and get the data from there directly
            if Language == "en":
                NewSearch = ""
                for i in Search:
                    if i == " ":
                        NewSearch += "_"
                    else:
                        NewSearch += i

                Link = "https://en.wikipedia.org/wiki/" + NewSearch

                source = urlopen(Link).read()  # reads the url
                soup = BeautifulSoup(source, "html.parser")  # uses html.parser
                text = ""  # makes the text file
                for paragraph in soup.find_all('p'):  # a for loop for the text under p
                    text += paragraph.text  # adds the text to the variable

                ListSplited = text.split(".")  # splits the text
                StringResult = ""  # for loop variable add
                for i in ListSplited:  # makes the foor loop
                    StringResult += i  # adds the value from ListSplited to StringResult
                    if NumOfSentences == 5:  # if x == 5
                        StringResult += "."  # adds a fullstop to the last sentence
                        break  # breaks
                NumOfSentences += 1  # x less than 5, adds 1 to the value x

                return StringResult


def search(Search, Language):
    """
    :param Search: Search
    :param Language: Language set by the user
    :return: A list of the searches that are connceted to the given
    """
    wikipedia.set_lang(Language) #sets language
    result = wikipedia.search(Search, 20) #gets 20 connections to the topic
    return result #return the results


def reference(Search, Language):
    """
    :param Search: Search
    :param Language: Language set by the user
    :return: a list of references
    """
    wikipedia.set_lang(Language)
    try:
        WikipediaClass = wikipedia.WikipediaPage(Search)  # makes the class
        result = WikipediaClass.references  # gets the refernces
    except:
        return None
    else:
        result = result[0:5]

        try:
            ReturnList = list(result)
            if len(ReturnList) == 0:
                return None
            return ReturnList
        except:
            return None


def Random(Language):
    """

    :param Language: Language from the server json
    :return: A summary of a random topic
    """
    if Language == "en":
        WikiClass = wikipediaapi.Wikipedia(language="en", extract_format=wikipediaapi.ExtractFormat.WIKI)  # initiates the wikipedia class
        wikipedia.set_lang("en")

        search = wikipedia.random(pages = 1)
        page = WikiClass.page(search)

        result = page.summary[:2500]
        ListSplited = result.split(".")

        NumberOfSentences = 0
        StringResult = ""

        for i in ListSplited:
            StringResult += i
            if NumberOfSentences == 5:
                StringResult += "."
                break
            NumberOfSentences += 1

        return StringResult

    else:
        return "This feature is only implemented for the English Language, please wait until it is updated."


def Images(Search):
    """

    :param Search: Title of what to search for
    :return: return a set of images
    """
    WikipediaClass = wikipedia.WikipediaPage(Search)  # makes the class
    result = WikipediaClass.images
    result = list(result[0:5])
    return set(result)


def Categories(Search, Language):
    """

    :param Search: The topic to find its Categories
    :param Language: The Language to use
    :return: returns a list of categories
    """
    WikiClass = wikipediaapi.Wikipedia(language = Language, extract_format = wikipediaapi.ExtractFormat.WIKI)

    page = WikiClass.page(Search)
    result = page.sections
    fresult = []
    for i in result:
        StringReturned = i.title
        fresult.append(StringReturned)
    return fresult


def Link(Search, Language):
    """

    :param Search:
    :param Language:
    :return:
    """
    wikipedia.set_lang(Language)
    try:
        WikipediaClass = wikipedia.page(search)
        result = WikipediaClass.url
        return result
    except:
        if Language != "en":
            return None
        else:
            NewSearch = ""
            for i in Search.lower():
                if i == " ":
                    NewSearch += "_"
                else:
                    NewSearch += i

            Link = "https://en.wikipedia.org/wiki/" + NewSearch

            try:
                source = urlopen(Link).read()
                soup = BeautifulSoup(source, "html.parser")
                return Link
            except:
                return None


def Test(Search, Language):
    """

    :param Search: Subject to test if page exists
    :param Language: Language to see if page exists
    :return: True or False depending on the result
    """
    WikiClass = wikipediaapi.Wikipedia(language = Language, extract_format = wikipediaapi.ExtractFormat.WIKI)
    page = WikiClass.page(Search)
    if page.exists():
        return True
    return False


def Section(Search, Language):
    """

    :param Search: Subject to gather its sections
    :param Language: Language to use
    :return: return a list with each index having a title, and 15 words
    """
    WikiClass = wikipediaapi.Wikipedia(language = Language, extract_format = wikipediaapi.ExtractFormat.WIKI)

    page = WikiClass.page(Search)
    result = page.sections
    fresult = []
    for i in result:
        StringReturned = ""
        StringReturned += i.title
        StringReturned += ": "
        StringReturned += i.text[:40]
        fresult.append(StringReturned)
    return fresult


def url(Search, Language):
    """

    :param Search: subject to search
    :param Language: Language used
    :return: returns a url
    """
    if Language != "en":
        return 1

    NewSearch = ""
    for i in Search.lower():
        if i == " ":
            NewSearch = "_"
        else:
            NewSearch += i

    Link = "https://en.wikipedia.org/wiki/" + NewSearch
    try:
        source = urlopen(Link).read()
        soup = BeautifulSoup(source, "html.parser")
        return Link
    except:
        return None


def Simple(Search, Language):
    """

    :param Search:
    :param Language:
    :return:
    """
    if Language != "en":
        return None
    SearchNSpace = ""
    for i in Search.lower():
        if i == " ":
            SearchNSpace += "_"
        else:
            SearchNSpace += i

    Link = "https://simple.wikipedia.org/wiki/" + SearchNSpace
    try:
        source = urlopen(Link).read()
        soup = BeautifulSoup(source, "html.parser")
        text = ""
        for i in soup.find_all("p"):
            text += i.text

        ListSplited = text.split(".")
        NumOfSentences = 0
        StringResult = ""
        for i in ListSplited:
            StringResult += i
            if NumOfSentences == 5:
                StringResult += "."
                break
            NumOfSentences += 1

        return StringResult
    except:
        return None
