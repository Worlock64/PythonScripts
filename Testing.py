import requests

#Gets requested URL from user
url = input('Please enter a URL: ')
response = requests.get(url)

#Test case to make sure url is valid.  Will return status code if not True
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))

#Included test case for vaild URL
response.raise_for_status()

print(response.text[:300] + '\n')

p= {"description":"white kitten",
    "name":"Snowball",
    "age_months": 6}

response = requests.post("https://example.com/path/to/api", data=p)

print(response.request.url)
print(response.request.body)
