from bs4 import BeautifulSoup # import libraries
import requests

# set up soup
page_to_scrape = requests.get("https://projects.fivethirtyeight.com/polls/president-general/2024/national/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# grabs all dates for most recent polls
dates = soup.find_all("td", class_="dates hide-desktop")
for date in dates:
    line1 = date.find("div") # extra removed (poll type if want to add later we need 2nd div)
    print(line1.text)

# grabs pollster names
pollsters = soup.find_all("td", class_="pollster")
for p in pollsters:
    print(p.text)

# gets all poll numbers tds (with names and numbers)
numbers = soup.find_all("td", class_="answers hide-desktop")
# gets all just biden numbers
for n in numbers:
    biden = n.find_all("div")[2]
    print("Biden", biden.text)

# gets all just trump numbers
for n in numbers:
    trump = n.find_all("div")[4]
    print("Trump", trump.text)