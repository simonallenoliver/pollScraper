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
tBody = myTable.find_all("tbody")[0]
for row in tBody.find_all('tr'):
    for td in row.find_all("td"):
        print(td)


# ---------Goals----------
# this is good start - eventually we need a way to get the swing state poll numbers as well
# all this needs to be entered into DB - reload once a day 
# using DB we can create model... some similarities to sand inventory transactions
# ...7.9.24... trying to figure out how to get all the data in a single query..