from django.contrib import admin
from . import models

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ['id','title', 'author']
	prepopulated_fields = {'slug': ('title',)}
