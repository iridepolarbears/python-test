import requests #for the website
import bs4 #to make it easier to view the data
import time #for the timer
from pymongo import MongoClient#for the database

client = MongoClient()
db = client['BBC']
headlines = db.headlines

def timer():
    query = input ("What news query would you like to search for on BBC? ")
    requestbbc(query)
    print('waiting a few seconds before the next prompt')
    time.sleep(10)#10 sec delay just in case


def requestbbc(input):

    print ('Searching for: ' + input)

    #request the info the user wants from BBC
    response = requests.get("https://www.bbc.co.uk/search?q="+input+
    "&filter=news")

    #use BeautifulSoup to get the edit the text
    soup_obj = bs4.BeautifulSoup(response.text,'lxml')

    print ('Title: '+ soup_obj.select('title')[0].getText())
    print()#print the title of the page and then a new line

    #get all the h1 tags and print them
    #this get all the titles with the h1 tag
    for anchor in soup_obj.findAll('h1'):
        print(anchor.string)

    print()
    print ('Another way to do this: ')
    print()
    line = {'Title': soup_obj.select('title')[0].getText()}
    result = headlines.insert_one(line)

    #this finds the actual headline itemprop and will print it
    for anchor in soup_obj.findAll(itemprop = 'headline'):
        print (anchor.string)
        line = {"Title": anchor.string}
        result = headlines.insert_one(line)

def printdb():
    #add in code to view the database
    for headline in headlines.find():
        print (headline['Title'])


def main():
    cont = True
    while cont == True:
        timer()
        inp = input('Would you like to search again? (enter y or n) ')
        if inp == 'y':
            cont = True
        elif inp == 'n':
            cont = False
            data = input('To print the database enter y: ')
            if data == 'y':
                print ('printing the current database: ')
                print()
                printdb()
            print ('exiting...')


if __name__ == "__main__":
    main()
