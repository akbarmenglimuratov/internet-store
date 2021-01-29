from django.db import models

class BaseNameSlug(models.Model):
	name = models.CharField(max_length = 250)
	slug = models.CharField(max_length = 250)

	class Meta:
		abstract = True

class Category(BaseNameSlug):

	sub_category = models.ForeignKey(
		'self', 
		on_delete = models.CASCADE, 
		related_name = "sub_categoryies", 
		blank = True, 
		null = True)

	def __str__(self):
		return self.name

class Manufacturer(BaseNameSlug):
	pass

class Goods(BaseNameSlug):

	category = models.ForeignKey(
		Category, 
		on_delete = models.CASCADE, 
		related_name = "goods_category")

	def __str__(self):
		return self.name