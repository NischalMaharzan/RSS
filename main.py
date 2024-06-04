from bs4 import BeautifulSoup
import requests

url = requests.get("https://au.onlinekhabar.com/feed")
# print(url)

soup = BeautifulSoup(url.content, "xml")
items = soup.find_all("item")
# //need to install parse to read xml file, i.e lxml, need to install lxml using pip 

for item in items:
    print(item.title)
    print(item.link)
    print(item.pubDate)
    print(item.category)
    print(item.guid)
    print(item.description)
    print("##################################################")

print(f"Total items: {len(items)}")