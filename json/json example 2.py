import json
# load and loads take input data and structure it as json data in python to be parsed
# load loads directly from a file we have opened
# https://www.geeksforgeeks.org/json-load-in-python/?ref=lbp
jsonFile = open("data.json", "r")  # open the data.json in read mode
jsonData = json.load(jsonFile)  # the load function takes the file handler jsonFile and loads its data directly to the variable
jsonFile.close()  # close the file
print(type(jsonData))  # we can see that it is saved as a list
print(jsonData)  # we print the list to see the data




# loads instead takes a string as an argument, so we would have to read and save the
# data of the document before passing it over to loads
# https://www.geeksforgeeks.org/json-loads-in-python/?ref=lbp
jsonFile = open("data.json", "r")  # open the data.json file again in read mode
jsonString = jsonFile.read()  # grab all the data from the file as a string, save it to a variable
# print(jsonString)  # this would print the whole contents of the file
jsonData2 = json.loads(jsonString)  # convert that string to structured json data and save it to a variable
print(type(jsonData2))  # we can see that it is a list, just like before
print(jsonData2)  # and that it is the same data as before
print(jsonData == jsonData2)  # double checking that they are indeed exactly the same




# dump takes the structured json data and puts it in a file
# https://www.geeksforgeeks.org/json-dump-in-python/?ref=lbp
dumpFile = open("dump.json", "w")  # open the file we are going to be writing to
json.dump(jsonData, dumpFile, indent=4)  # take the structured data we extracted earlier and write it to a new file
dumpFile.close()  # save and close the file





# dumps takes structured data and returns what it looks like as a string
# opposite of loads
# https://www.geeksforgeeks.org/json-dumps-in-python/?ref=lbp

dumpsOutput = json.dumps(jsonData, indent=4)  # take the document string and write it to the new file
dumpsFile = open("dumps.json", "w")  # open the file to write to
dumpsFile.write(dumpsOutput)
dumpsFile.close()  # save and close the file


input()
