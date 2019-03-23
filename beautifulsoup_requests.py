import requests #for the website
import bs4 #to make it easier to view the data
import time #for the timer

def timer():
    query = input ("What news query would you like to search for on BBC? ")
    request(query)


def request(input):

    print ('searching for: ' + input)

    #request the info the user wants from BBC
    response = requests.get("https://www.bbc.co.uk/search?q="+input+
    "&filter=news")

    #use BeautifulSoup to get the edit the text
    soup_obj = bs4.BeautifulSoup(response.text,'lxml')

    print(soup_obj.select('title')[0].getText())#print the title of the page

    #get all the h1 tags and print them
    for anchor in soup_obj.findAll('h1'):
        print(anchor.string)

def main():
    cont = True
    while cont == True:
        timer()
        inp = input('would you like to search again? (enter y or n)')
        time.sleep(10)#delay of 10 seconds just in case there's a request delay
        if inp == 'y':
            cont = True
        elif inp == 'n':
            cont= False

if __name__ == "__main__":
    main()
