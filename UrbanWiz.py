"""
Basic web scraper for UrbanDictionary
Feel free to add any improvements :)
"""


from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

BASE_URL = "http://www.urbandictionary.com"

def get_definition_link(section_url):
    word_url = BASE_URL + "/define.php?term="+section_url
    response = requests.get(word_url)
    html = urlopen(response.url).read()
    # soup = BeautifulSoup(html, "lxml")
    return response.url

def read_definition(word_url):
    html = urlopen(word_url)
    soup = BeautifulSoup(html,"lxml")
    try:
        definition = soup.find("div","meaning").text
        word = soup.find("a","word").string
    except:
        definition = " isn't defined :O"
        word = "NULL"
    return [word,definition]


def main():
    print("Type 'exit' to close")
    x = ""
    while x != "exit":
        try:
            x = str(input("What you tryna say? ")).lower().replace(" ","+")
        except ValueError:
            print("Sorry, error :(")
        retList=read_definition(get_definition_link(str(x)))
        retList[1]=retList[1].replace("\r","\n\n~ ")

        if retList[0]!="NULL":

            print(str(retList[0])+": \n"+"~ "+retList[1][1:])
        else:
            print('"'+x+'"'+retList[1])

    print("\nThanks for using!")
if __name__ == "__main__":
    main()
