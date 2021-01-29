from django.urls import path
from . import views

urlpatterns = [
	path('', views.BlogListView.as_view()),
	path('<slug:slug>/', views.BlogDetailView.as_view())
]