import logging
# we're logging stuff
from datetime import date
from datetime import datetime
# datetime reference
# https://www.programiz.com/python-programming/datetime/strftime
now = datetime.now()
current_time = now.strftime("%m-%d-%Y at %H-%M-%S")
# Returns the current local date
# today = date.today()
# todayString = today.strftime("%m-%d-%Y at ")
# ("Today date is: ", today)
logFileName = "./logs/" + current_time + ".txt"
someNumber = 10
logging.basicConfig(filename=logFileName, level=logging.DEBUG)
logging.debug(f"number is currently {someNumber}")
logging.warning("something caused a warning")
logging.error("something caused an error")
logging.critical("Christian, HELP!")
try:
    x = int("a")
except:
    logging.exception("We caused an exception here")
