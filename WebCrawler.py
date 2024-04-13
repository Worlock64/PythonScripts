import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
#import ssl

#Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL - ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

total = 0

'''
tags = soup('span')
for tag in tags:
    text = tag.get_text()
    matches = re.findall(r'\d+', text)

    for number in matches:
        total += int(number)


print(total)
'''

tags = soup('a')
for tag in tags:
    next_link = tag.get('href')
    print(next_link)