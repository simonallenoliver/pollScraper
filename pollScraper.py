from bs4 import BeautifulSoup # import libraries
import requests

# -------web scraping basics--------
# Beautiful Soup helps parse HTML and extract data, 
# while Selenium handles dynamically loaded content.
# Always check a website’s robots.txt file to see if 
# scraping is allowed.

# ---------set up soup--------------
page_to_scrape = requests.get("https://www.realclearpolling.com/polls/president/general/2024/trump-vs-biden")
# rcp ended up being much more difficult to work with compared to 538
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# find will get the first item matching the criteria
# findAll will gett all the items matching the criteria
# example: this will find all the table rows with the exact class listed below
# in this case it is only one row

# finds table at index 1 (second table in soup) and assigns it to var called my_table
my_table = soup.find_all("table")[1]
# print(my_table)


# finds and prints all table heads in soup
# global_titles = soup.find_all("th")
# for title in global_titles:
#     print(title.text)

# finds only table head in my_table
my_table_titles = my_table.find_all("th")
for title in my_table_titles:
    print(title.text)



# Find all rows within the table
table_rows = my_table.find_all('tr')

# Iterate through the rows and print the text inside each <td> tag
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)