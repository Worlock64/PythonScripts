import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def findNextPerson(url, position):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    curpos = 0
    tags = soup('a')

    for tag in tags:
        next_link = tag.get('href', None)
        curpos +=1
        if curpos == position:
            break
    
    return next_link

curCount = 0

url = input("Enter starting URL - ")
positionstr = input('Enter the positon of the person - ')
position = int(positionstr)
totalCountstr = input('Enter the total number of people you wish to find - ')
totalCount = int(totalCountstr)
curURL = url

while curCount != totalCount:
    curURL = findNextPerson(curURL, position)
    curCount+=1

print(curURL)