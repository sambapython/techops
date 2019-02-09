from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	user_types=[('e',"Employee"),('m',"Manager")]
	phone=models.CharField(max_length=10)
	type=models.CharField(choices=user_types, max_length=1)

class LeaveType(models.Model):
	name=models.CharField(max_length=250)
	count=models.IntegerField()

	def __str__(self):
		return self.name

class Leave(models.Model):
	desc=models.TextField(blank=True, null=True)
	type=models.ForeignKey(LeaveType, on_delete=models.PROTECT)
	# models.CASCADE: if you delete leave type, then it will delete all the leaves belongs 
	# to that type
	#models.PROTECT: if you delete any leave type, it wont allow you to delete the type
	# if it has any leaves with that type in the leave table
	date=models.DateTimeField(default=datetime.now)
	leavedate=models.DateField()
	user=models.ForeignKey(User, on_delete=models.PROTECT)
