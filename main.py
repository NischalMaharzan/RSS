from bs4 import BeautifulSoup
import requests
from database import database_connection



url = requests.get("https://au.onlinekhabar.com/feed")
# print(url)

soup = BeautifulSoup(url.content, "xml")
items = soup.find_all("item")
# //need to install parse to read xml file, i.e lxml, need to install lxml using pip 


# //DB CONNECTION and established a db session as conn
conn = database_connection()
print(conn)
cur = conn.cursor()
cur.execute("CREATE TABLE articles (id serial PRIMARY KEY, title varchar, link varchar, description varchar);")



for item in items:
    title = item.title.text
    link = item.link.text
    pubDate = item.pubDate.text
    category = item.category.text
    des = item.description.text
    print(f"Title: {title} \nDate: {pubDate} \nCategory: {category} \nDescription: {des} \nLINK: {link}", "#"*50, sep='\n')
    cur.execute("INSERT INTO articles (title, link, description) VALUES (%s, %s, %s)",(title, link, des))
    conn.commit()


cur.close()
conn.close()

print(f"Total items: {len(items)}")
   
