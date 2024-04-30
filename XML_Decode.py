import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url =input('Enter the URL: ')

urlhandle = urllib.request.urlopen(url)
data = urlhandle.read()

tree = ET.fromstring(data)
counts = tree.findall('.//count')

total_comments = sum(int(count.text) for count in counts)

print('Total sum: ', total_comments)