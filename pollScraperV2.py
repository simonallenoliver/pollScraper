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

# grabs all dates for most recent polls
allDates = []
dates = soup.find_all("td", class_="dates hide-desktop")
for date in dates:
    line1 = date.find("div") # extra removed (poll type if want to add later we need 2nd div)
    allDates.append(line1.text)


# grabs pollster names
allPollsters = []
pollsters = soup.find_all("td", class_="pollster")
for p in pollsters:
    allPollsters.append(p.text)

for p in allPollsters:
    sql = "INSERT INTO polls (bidenPercent, trumpPercent, date, pollster, createdAt, updatedAt) VALUES (%s, %s, %s, %s, %s, %s)"
    # these vaues will be our variable from below - this will prob go after the scraping stuff
    val = (39, 61, now, p, now, now)
    mycursor.execute(sql, val)
    mydb.commit()
# -----------------wow ok cool managed to get all the pollsters added to the db in one go
# need to figure out how to add all the data in one query

# gets all poll numbers tds (with names and numbers)
numbers = soup.find_all("td", class_="answers hide-desktop")
# gets all just biden numbers
allBiden = []
for n in numbers:
    biden = n.find_all("div")[2]
    allBiden.append(biden.text)

# gets all just trump numbers
allTrump = []
for n in numbers:
    trump = n.find_all("div")[4]
    allTrump.append(trump.text)

# this will be a list of lists, maybe we want it to be a dictionary of lists?
allData = []
# aggregate all the data
allData.append(allDates)
allData.append(allPollsters)
allData.append(allBiden)
allData.append(allTrump)
print("ALL DATA START",allData,"ALL DATA END")


# ---------Goals----------
# this is good start - eventually we need a way to get the swing state poll numbers as well
# all this needs to be entered into DB - reload once a day 
# using DB we can create model... some similarities to sand inventory transactions
# ...7.9.24... trying to figure out how to get all the data in a single query..