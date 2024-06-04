from bs4 import BeautifulSoup
import requests

url = requests.get("https://au.onlinekhabar.com/feed")
# print(url)

soup = BeautifulSoup(url.content, "xml")
items = soup.find_all("item")
# //need to install parse to read xml file, i.e lxml, need to install lxml using pip 

for item in items:
    title = item.title.text
    link = item.link.text
    pubDate = item.pubDate.text
    category = item.category.text
    des = item.description.text
    print(f"{title}, {pubDate}, {category}, {des}, {link}", '#'*50, sep='\n')

print(f"Total items: {len(items)}")