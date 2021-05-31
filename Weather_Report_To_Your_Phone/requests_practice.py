from bs4 import BeautifulSoup
import requests

source = requests.get("https://coreyms.com/").text

soup = BeautifulSoup(source, 'lxml')

article = soup.find("article")

#print(article.prettify())

#headline = article.h2.a.text
#print(headline)

# summary = article.find("div", class_ = "entry-content").p.text
# print(summary)

#todo ctrl + / to comment the codes.

'''vid_src = article.find("iframe", class_="youtube-player")
print(vid_src)
vid_src = article.find("iframe", class_="youtube-player")['src'] # see the codes like dictionary.
print(vid_src)

vid_id = vid_src.split("/")
print(vid_id)
vid_id = vid_id[4]
print(vid_id)
vid_id = vid_id.split("?")
print(vid_id)
vid_id = vid_id[0]
print(vid_id)

yt_link = f"https://youtube.com/watch?v={vid_id}"
print(yt_link)'''
for article in soup.find_all("article"):
    headline = article.h2.a.text

































