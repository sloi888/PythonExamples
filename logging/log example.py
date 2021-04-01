import logging
from datetime import date
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H-%M-%S")
print("Current Time =", current_time)
# Returns the current local date
today = date.today()
todayString = today.strftime("%m-%d-%Y at ")
print("Today date is: ", today)
logFileName = "./logs/" + todayString + current_time + ".logg"
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
