from bs4 import BeautifulSoup  # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import pandas as pd

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html)

print(soup.prettify())
#The Tag object corresponds to an HTML tag in the original document, for example, the tag title.
tag_object = soup.title
print(f"tag totle: {tag_object}")
print("tag object type:",type(tag_object))

# If there is more than one Tag with the same name, the first element with that Tag name is called, this corresponds to the most paid player:
tag_h3 = soup.h3
print(f"tag h3: {tag_h3}")

tag_child = tag_h3.b
print(f"child tag b of h3: {tag_child}")
print(f"parents tage of tag_child: {tag_child.parent} ")

#tag_object sibling is the paragraph element
sibling_1=tag_h3.next_sibling
print(f"sbling of of h3: {sibling_1}")

sibling_2=sibling_1.next_sibling
print(f"sbling of of h3: {sibling_2}")

#If the tag has attributes, the tag id="boldest" has an attribute id whose value is boldest.
#We can access a tag’s attributes by treating the tag like a dictionary
print(f"attribute of b tag: {tag_child['id']}")
print(f"attribute of b tag: {tag_child.get('id')}")
print(f"all attributes of b tag: {tag_child.attrs}")

#A string corresponds to a bit of text or content within a tag.
# Beautiful Soup uses the NavigableString class to contain this text.
print(f"Navigatable string: {tag_child.string}")
print(f"Navigatable string: {type(tag_child.string)}")


# Filters allow you to find complex patterns, the simplest filter is a string.
# In this section we will pass a string to a different filter method
# and Beautiful Soup will perform a match against that exact string.

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table)
print(table_bs.prettify())

#The Method signature for find_all(name, attrs, recursive, string, limit, **kwargs)
table_rows=table_bs.find_all('tr')
print(f"all rows of table: {table_rows}")

first_row= table_rows[0]
print(f"first row: {first_row}")
print(f"Type of row: {type(first_row)}")
print(f"child of first row: {first_row.td}")

for i,row in enumerate(table_rows):
    print("row",i,"is",row)

for i,row in enumerate(table_rows):
    print("row",i)
    cell = row.find_all('td')
    for j,text in enumerate(cell):
        print('colunm',j,"cell",cell)

list_input=table_bs.find_all(name=["tr", "td"])
print(f"list with multiple match: {list_input}")

list_with_href=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print(f"list_with_href : {list_with_href}")

print(f"all tags with href attribute: {table_bs.find_all(href=True)}")
# all without href: table_bs.find_all(href=False)

all_with_Floria_string = table_bs.find_all(string="Florida")
print(f"all strings with given string: {all_with_Floria_string}")

#find() method to find the first element in the document.

#here is two tables Rocket Launch, Pizza Party
two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"

two_tables_bs= BeautifulSoup(two_tables)
print(two_tables_bs.prettify())
class_pizzza= two_tables_bs.find("table",class_='pizza')
fiest_table = two_tables_bs.find("table")
print(f"first table : {fiest_table}")
print(f"first table by class attribute : {class_pizzza}")

#Downloading And Scraping The Contents Of A Web Page

url = "http://www.ibm.com"
data  = requests.get(url).text
webPageConetent = BeautifulSoup(data)
print(f"website conetnt: {webPageConetent.prettify()}")

#Scrap all links
for link in webPageConetent.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
    print(f"hyper link : {link.get('href')}")

#Scrap all imges

for link in webPageConetent.find_all('img'): # in html image is represented by the tag <img>
    print(f"link: {link}")
    print(f"{link.get('src')}")

#Scrape data from HTML tables

#The below url contains an html table with data about colors and color codes.
urlForTables = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

htmlTable = requests.get(urlForTables).text
soupWebText = BeautifulSoup(htmlTable)
print(f"web text: {soupWebText.prettify()}")
webTable = soupWebText.find('table')
#all rows frm table

#Get all rows from the table
for row in webTable.find_all('tr'):
    # Get all columns in each row.
    cols = row.find_all('td')
    color_name = cols[2].string
    color_code = cols[3].string
    print("{}--->{}".format(color_name,color_code))


#Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas
urlForPopulationData = "https://en.wikipedia.org/wiki/World_population"
#The below url contains html tables with data about world population.
data  = requests.get(urlForPopulationData).text
populationData = BeautifulSoup(data)
populationTables = populationData.find_all('table')
print(f"lenth of population : {len(populationTables)}")

table_index = 0
for index,table in enumerate(populationTables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index

print(f"index of 10 most densely populated countries table:  {table_index}")

print(populationTables[table_index].prettify())

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in populationTables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

print(f"Population data: {population_data}")

#The function read_html always returns a list of DataFrames so we must pick the one we want out of the list.
#
# population_data_read_html = pd.read_html(str(populationTables[5]))
#
# print(f"population_data_read_html: {population_data_read_html[0]}")

urlForPopulationData = "https://en.wikipedia.org/wiki/World_population"
data_with_pd = pd.read_html(urlForPopulationData, flavor='bs4')
print(f"Population data with read_html: {data_with_pd}")
pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]



# Notes:
#Beautiful Soup is a Python library for pulling data out of HTML and XML files
#First, the document is converted to Unicode, (similar to ASCII), and
# HTML entities are converted to Unicode characters. Beautiful Soup transforms a complex HTML document
# into a complex tree of Python objects. The BeautifulSoup object can create other types of objects.

# . Beautiful Soup transforms a complex HTML document into a complex tree of Python objects. The BeautifulSoup object can create other types of objects. In this lab, we will cover BeautifulSoup and
# Tag objects that for the purposes of this lab are identical, and NavigableString objects.
#
