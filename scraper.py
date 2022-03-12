
from urllib.request import urlopen
import re

url = "https://www.inspiringinterns.com/job-board/all"
#page = urlopen(url)
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
#print(html)

title_index = html.find("<title>")
title_index
start_index = title_index + len("<title>")
start_index
end_index = html.find("</title>")
end_index
title = html[start_index:end_index]

url3 = "https://www.inspiringinterns.com/job-board/all"
page = urlopen(url3)

html = page.read().decode("utf-8")

pattern = "<h1(.*?)>.*?</h1>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)