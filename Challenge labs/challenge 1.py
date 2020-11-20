# filemaker.py
from datetime import date
import os
number = 1
DATE = date.today().strftime("%b-%d-%Y") # save the date in month-day-year format as a string
name = input("What is your name? ")
directory = f"./{name}-{DATE}"
currentFile = name + str(number)
#echo currentFile
if os.path.isdir(directory):
  print(f"{directory} already exists")
else:
  print(f"creating {directory}")
  os.mkdir(directory)

filesCreated = 0
while filesCreated < 25:
  if os.path.isfile(f"{directory}/{currentFile}"):
    print(f"{currentFile} already exists, skipping...")
    number += 1
    #print(number)
    #print(filesCreated)
    currentFile = name + str(number)
  else:
    print(f"Creating {currentFile}")
    file = open(f"{directory}/{currentFile}", "x")
    file.close()
    #os.system(f"touch {directory}/{currentFile}")
    number += 1
    filesCreated += 1
    currentFile = name + str(number)
