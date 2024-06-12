from bs4 import BeautifulSoup # import libraries
import requests

# set up soup
page_to_scrape = requests.get("https://www.realclearpolling.com/polls/president/general/2024/trump-vs-biden")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# find will get the first item matching the criteria
# findAll will gett all the items matching the criteria
# example: this will find all the table rows with the exact class listed below
# in this case it is only one row

# finds table at index 1 (second table in soup) and assigns it to var called my_table
my_table = soup.find_all("table")[1]


# finds and prints all table heads in soup
global_titles = soup.find_all("th")
# for title in global_titles:
#     print(title.text)

# finds only table head in my_table
my_table_titles = my_table.find_all("th")
# for title in my_table_titles:
#     print(title.text)

# column_data = my_table.find_all('tr')

# for row in column_data:
#     row_data = row.find_all('td')
#     individual_row_data = [data.text for data in row_data]
#     print(individual_row_data)

# example of combining disparate data
# for quote, author in zip(quotes, authors):
#     print(quote.text + " - " + author.text)