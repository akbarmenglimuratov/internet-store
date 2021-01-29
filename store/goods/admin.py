from django.contrib import admin
from goods import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(models.Goods)
class GoodsAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(models.Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'slug']
	prepopulated_fields = {'slug': ('name',)}