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

    line = {'Title': soup_obj.select('title')[0].getText()}
    headlines.insert_one(line)

    #this finds the actual headline itemprop and will print it
    #also push it into the database

    for anchor in soup_obj.findAll(itemprop = 'headline'):
        a_tag = anchor.next_element #get the web link tag from headline
        link = a_tag['href']#get the actual link
        #get the info from the url
        headline_in = headline_info(link)#get the headline info from the link
        if headline_in is not 'no':
            print (anchor.string + ': ' + headline_in)
            print()
            line = {
                    "Title": anchor.string + ': ' + headline_in
                    }
            result = headlines.insert_one(line)

def headline_info (link):
    response = requests.get(link)
    web = bs4.BeautifulSoup(response.text,'lxml')
    anchor = web.find('p', {'class' : 'story-body__introduction'})
    if anchor is not None:
        return anchor.string
    else:
        return 'no'


def printdb():
    #add in code to view the database
    for headline in headlines.find():
        print (headline['Title'])
        print()


def main():
    cont = True
    while cont == True:
        timer()
        inp = input('Would you like to search again? (enter y or n) ')
        if inp == 'y':
            cont = True
        elif inp == 'n':
            cont = False
            print ('printing the current database: ')
            print()
            printdb()
            #remove the database
            db.headlines.remove(){}
            print ('exiting...')
            exit()


if __name__ == "__main__":
    main()
