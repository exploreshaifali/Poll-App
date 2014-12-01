from django.db import models

# Create your models here.

class Article(models.Model):
	"""docstring for Article"""
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField()
	likes = models.IntegerField()

