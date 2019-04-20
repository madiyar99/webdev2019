from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index),
	path('about', views.about),
	path('date', views.current_time),
	path('products/<int:pk>/', views.show_product),
	path('category', views.category_list)
]