from django.db import models

class BaseNameSlug(models.Model):
	name = models.CharField(max_length = 250)
	slug = models.SlugField(max_length = 250)

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
	
	def __str__(self):
		return self.name

class Goods(BaseNameSlug):

	category = models.ForeignKey(
		Category,
		on_delete = models.SET_NULL,
		null = True,
		related_name = "goods_category")

	def __str__(self):
		return self.name

def goods_pic_upload(instance, filename):
	return "movie_shots/{0}/{1}".format(instance.name,filename)
class GoodsPicture(models.Model):

	image = models.ImageField(upload_to = goods_pic_upload)
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE, related_name = "goods_picture")
