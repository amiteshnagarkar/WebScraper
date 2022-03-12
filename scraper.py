
from urllib.request import urlopen


url2 = "https://www.deployers.co.uk/"
#page = urlopen(url)
page = urlopen(url2)

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

#prints the title h1 tag
print(title)
