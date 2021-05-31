from bs4 import BeautifulSoup
import requests

with open("simple.html") as html_file: # read the file is default
    soup = BeautifulSoup(html_file, "lxml")

'''match = soup.div
print(match)
match = soup.find("div", class_="footer")
print(match)'''

'''for article in soup.find_all('div', class_ = "article"): # because class is default in python, we need to use class_

    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
    print()'''






































