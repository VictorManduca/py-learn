from django.db import models

class UserModel(models.Model):
	name = models.TextField()
	age = models.IntegerField()

	def  __str__(self):
		return self

		