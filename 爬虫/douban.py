from bs4 import BeautifulSoup
import pymysql
import requests
import re
db=pymysql.connect("localhost","root","123","douban")
cursor=db.cursor()
kv = {'user-agent': 'Mozilla/5.0'}
for i in range(4):
 html=requests.get("https://movie.douban.com/top250?start={0}".format(i*25),headers=kv,timeout =30).text.replace("\n","")

 soup = BeautifulSoup(html, 'html.parser')
 alist=soup.find_all(class_ ="item")

 for a in alist:
  title=re.search(r"class=\"title\">(.+?)</span>",str(a), re.M|re.I).group(1)
  img = re.search(r"<img.*src=\"(.+?)\".*>", str(a), re.M | re.I).group(1)
  dirandtype = re.search(r"(导演.+?)<br/>(.+?)</p>", str(a), re.M | re.I)
  star = re.search(r"property=\"v:average\">(.+?)</span>", str(a), re.M | re.I).group(1)
  director=dirandtype.group(1)
  type=dirandtype.group(2)
  sql="insert into movie(name,poster,people,type,star) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(db.escape_string(title),db.escape_string(img),db.escape_string(director),db.escape_string(type),db.escape_string(star))

  print(sql)
  cursor.execute(sql)
  db.commit()
  print(title)
  print(img)
  print(director)
  print(type)
  print(star)
db.close()