import urllib.request
import json

url = input("Enter the URL: ")

urlhandle = urllib.request.urlopen(url)
data = json.load(urlhandle)

counts = [item['count'] for item in data['comments']]

total_comments = sum(counts)

print("Sum of comment counts:", total_comments)