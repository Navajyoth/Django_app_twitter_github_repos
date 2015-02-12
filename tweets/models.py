from django.db import models

# Create your models here.

class User(models.Model):
	user_name = models.CharField(max_length = 25)
	count = models.CharField(max_length = 6)

	def __unicode__(self):
		return self.user_name
