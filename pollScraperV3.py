from bs4 import BeautifulSoup # import libraries
import requests
import datetime

# connection to mysql (had to install mysql python connector)
# connection tested successfully
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="pollscraperdb"
)

mycursor = mydb.cursor()

# create var for current date time - may change to just date?
now = datetime.datetime.now()



# set up soup
page_to_scrape = requests.get("https://projects.fivethirtyeight.com/polls/president-general/2024/national/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

myTable = soup.find_all("table")[1]
tRows = myTable.find_all("tr")
for row in tRows:
    print(row.text)

# --------------7.10.24 uhg why is this not working; both the above and below attempts only produced the first
# few rows of the table - may be an issue with multiple table bodies? unclear and this is annoying

# for tBody in tBods:
#     print("t BOD", tBody.text)
#     tRows = tBody.find_all("tr")
#     # mayhaps the sql query goes here.... it will go through each row, and the tds will be the indi data
#     for row in tRows:
#         print(row.text)


# ---------Goals----------
# this is good start - eventually we need a way to get the swing state poll numbers as well
# all this needs to be entered into DB - reload once a day 
# using DB we can create model... some similarities to sand inventory transactions
# ...7.9.24... trying to figure out how to get all the data in a single query..