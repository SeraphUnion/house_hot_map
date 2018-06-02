from django.db import models 
from django.contrib.auth.models import User 
class taizhou(models.Model): 
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=100)
	cityid = models.CharField(max_length=10)
	info = models.TextField(blank=True)
	mi2=models.BigIntegerField()
	tel = models.TextField(blank=True)
	avg=models.BigIntegerField(null=True)
	howsell= models.TextField(null=True)
	getdate = models.DateTimeField()
	GPS_lat = models.TextField(null=True)
	GPS_lng = models.TextField(null=True)
