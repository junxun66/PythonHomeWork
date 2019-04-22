from django.shortcuts import render
import pymysql
from django.shortcuts import HttpResponse
# Create your views here.

def Index(request):
    return  render(request,"index.html")
def Home(request):
    moveList = []
    if request.method=="GET":
        start = 0
        try:
          start=request.GET.get("start")


          start=int(start)

        except:
            start = 0
        print(start)
        db = pymysql.connect("localhost", "root", "123", "douban")
        cursor=db.cursor()

        sql="select  *  from movie limit {0},{1}".format(start,start+24)
        cursor.execute(sql)
        alldata=cursor.fetchall()
        for row in alldata:

            name = row[1]
            poster = row[2]
            people = row[3]
            type = row[4]
            star = row[5]
            moveList.append({"name":name,"poster":poster,"people":people,"type":type,"star":star})
    db.close()
    return  render(request,"Home.html",{"movieList":moveList})