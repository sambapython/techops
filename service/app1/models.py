from django.db import models

# Create your models here.
class Customer(models.Model):
	name=models.CharField(max_length=250)
	email=models.CharField(max_length=250, blank=True)

	def __str__(self):
		return "%s,%s"%(self.name,self.email)
