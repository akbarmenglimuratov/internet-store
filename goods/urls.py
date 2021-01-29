from django.urls import path, include
from . import views

urlpatterns = [
	path('<slug:slug>/', views.CategoryViews.as_view()),
]