import requests
import re
from bs4 import BeautifulSoup

URL = "https://www.bbcgoodfood.com/recipes/padron-peppers"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

name = soup.find("h1", class_="heading-1").text
author = soup.find("a", rel="author").text
description = soup.find("div", class_="editor-content").find("p").text

rating_count = int(soup.find("span", class_="rating__count-text").text.replace(" ratings", ""))
rating_value_text =  soup.find("div", class_="rating__values").find("span", class_="sr-only").text
rating_value = re.search(".*of (.*) out of (.*).*",rating_value_text,re.IGNORECASE).group(1)

print(name)
print(author)
print(description)
print(rating_count)
print(rating_value)