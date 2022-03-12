
from urllib.request import urlopen
import re

#gets first h1 tag, using regular exp
#regular exp not useful for printing all titles.
url = "https://www.inspiringinterns.com/job-board/all"
page = urlopen(url)
html = page.read().decode("utf-8")
pattern = "<h1(.*?)>.*?</h1>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
#Remove HTML tags
title = re.sub("<.*?>", "", title)
#print(title)

#----------------------------------------

#BeautifulSoup

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
#does same thing as above
#print(soup.h1.string)

# retreives all job titles from page 1
heading_tags = ["h1"]
for tags in soup.find_all(heading_tags):
    print(tags.text.strip())


