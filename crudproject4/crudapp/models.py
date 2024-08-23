from django.db import models
class Employee(models.Model):
	no=models.IntegerField()
	name=models.CharField(max_length=64)
	sal=models.IntegerField()
	exp=models.CharField(max_length=100)