
from urllib.request import urlopen
import re

#gets first h1 tag, using regular exp
#regular exp not useful for printing all titles.

#pattern = "<h1(.*?)>.*?</h1>"
#match_results = re.search(pattern, html, re.IGNORECASE)
#title = match_results.group()
#Remove HTML tags
#title = re.sub("<.*?>", "", title)
#print(title)

#----------------------------------------

#BeautifulSoup


from bs4 import BeautifulSoup
import requests

#url = "https://www.inspiringinterns.com/job-board/all"
#page = urlopen(url)
#html = page.read().decode("utf-8")


page = 1
job_titles = []

while page != 50:
      url = f"https://www.inspiringinterns.com/job-board/all?page={page}"
      response = requests.get(url)
      html = response.content
      soup = BeautifulSoup(html, "html.parser")
      #heading_tags = ["h1"]
      for h1 in soup.find_all("h1", class_="hide-for-mobile"):
            job_titles.append(h1.get_text(strip=True))
      page = page + 1
len(job_titles)

#prints n number of job titles, regardless of page number, there are 50 pages.
n=10
for title in job_titles[:n]:
    print(title)




#does same thing as above
#print(soup.h1.string)

# retreives all job titles from page 1
#heading_tags = ["h1"]
#for tags in soup.find_all(heading_tags):
    #print(tags.text.strip())


