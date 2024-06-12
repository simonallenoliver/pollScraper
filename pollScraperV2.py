from bs4 import BeautifulSoup # import libraries
import requests

# set up soup
page_to_scrape = requests.get("https://projects.fivethirtyeight.com/polls/president-general/2024/national/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# grabs all dates for most recent polls
dates = soup.find_all("td", class_="dates")
for date in dates:
    line1 = date.find("div") # extra removed (poll type if want to add later we need 2nd div)
    print(line1.text)