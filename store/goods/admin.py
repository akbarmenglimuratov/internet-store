from django.contrib import admin
from goods import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(models.Goods)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']
	prepopulated_fields = {'slug': ('name',)}