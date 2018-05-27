
您可以使用 SQLite .schema 命令得到表的完整信息，如下所示
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


SQLite 存储类
每个存储在 SQLite 数据库中的值都具有以下存储类之一：

SQLite 的存储类稍微比数据类型更普遍。INTEGER 存储类，例如，包含 6 种不同的不同长度的整数数据类型。
SQLite 亲和(Affinity)类型
SQLite支持列的亲和类型概念。任何列仍然可以存储任何类型的数据，当数据插入时，该字段的数据将会优先采用亲缘类型作为该值的存储方式。SQLite目前的版本支持以下五种亲缘类型：

SQLite 亲和类型(Affinity)及类型名称
下表列出了当创建 SQLite3 表时可使用的各种数据类型名称，同时也显示了相应的亲和类型：

