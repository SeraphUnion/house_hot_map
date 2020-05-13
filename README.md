 1、git clone git@github.com:cangtianyx/house_hot_map.git
 
 2、sudo apt-get install python3 python3-pip screen sqlite3
 
 3、pip3 install bs4 django requests lxml
 
 4、python3 manage.py runserver 192.168.31.xxx:8000（本机ip）
 
 5、screen 切换服务进程到后台
 
 6、python3 fangchan.py 抓取数据到db.sqlite。
 
 7、浏览器开启 192.168.31.xxx:8000
 
======================================================

1、您可以使用 SQLite .schema 命令得到表的完整信息，如下所示：
sqlite3
.open db.sqlite3
.schema

CREATE TABLE taizhou
           (
           id             integer PRIMARY KEY autoincrement, 
           name           TEXT,
           info           TEXT,
           mi2            NUMERIC,
           tel            TEXT,
           avg            NUMERIC,
           howsell        TEXT,
           getdate        TEXT,
           GPS_lat        TEXT,
           GPS_lng        TEXT);

2、django MTV中的M设置：

blog/models.py

from django.db import models

from django.contrib.auth.models import User

class taizhou(models.Model):

	id = models.BigAutoField(primary_key=True)
	
	name = models.CharField(max_length=100)
	
	info = models.TextField(blank=True)
	
	mi2=models.BigIntegerField()
	
	tel = models.TextField(blank=True)
	
	avg=models.BigIntegerField()
	
	howsell= models.TextField(blank=True)
	
    	getdate = models.DateTimeField()
	
	GPS_lat = models.TextField(blank=True)
	
	GPS_lat = models.TextField(blank=True)


