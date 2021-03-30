# you may need to install requests with pip
# you should be able to install pip alongside your python installation
# if you didn't then you can get it here https://pip.pypa.io/en/stable/installing/
# 'pip install requests' in your terminal

import json
import requests
import random

# this function is used when we sort the data we get later
def byTitle(d):
    return d['title']


def byID(d):
    return d['id']
# use requests to download a sample json file from the internet https://realpython.com/python-json/
response = requests.get("https://jsonplaceholder.typicode.com/todos")
data = json.loads(response.text)
dataFile = open("data.json", "w")
json.dump(data, dataFile, indent=4)
dataFile.close()

# sort the data by title. If you want to sort by other criteria, follow the example of the above function
# and then make the key= parameter that function's name
data.sort(key=byTitle)
# open the file 'sortedByTitle.json' in write mode
byTitleFile = open("sortedByTitle.json", "w")
# dump the data into the sortedByTitle.json with an indentation per level of 4
json.dump(data, byTitleFile, indent=4)
# save the changes to the file and stop accessing it
byTitleFile.close()

# does the same as above but with a different sort and to a different file
# this one sorts the data by ID (which isn't helpful in this case since it already is by default)
# but I'll keep it here as an example
data.sort(key=byID)
byIDFile = open("sortedByID.json", "w")
json.dump(data, byIDFile, indent=4)
byIDFile.close()

# this time we scramble the data
random.shuffle(data)
scrambledFile = open("scrambledData.json", "w")
json.dump(data, scrambledFile, indent=4)
scrambledFile.close()
