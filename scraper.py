
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
import pandas as pd

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
      
      
      
      for h1 in soup.find_all("h1", class_="hide-for-mobile"):
            job_titles.append(h1.get_text(strip=True))
      page = page + 1
#print(len(job_titles))
#print(job_titles)


result = list(filter(lambda x: "Data" in x, job_titles))
n=588 #use result of print(len(job_titles))

data_jobs = []
for title in result[:n]:
    #print(title)
    #data_jobs = [title]
    data_jobs.append(title)
    df = pd.DataFrame(data_jobs)
    writer = pd.ExcelWriter('InspiringInterns-DJ.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Data Jobs', index=False)
    writer.save()

