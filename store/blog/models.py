from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):

	title = models.CharField(max_length = 255)
	slug = models.SlugField(max_length = 255)
	text = models.TextField()
	author = models.ForeignKey(
		User, 
		on_delete = models.CASCADE, 
		related_name = "blog_author")
