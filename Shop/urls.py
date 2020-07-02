from django.urls import path

from . import views

urlpatterns = [
	path('get-shop-groceries/<int:pk>', views.ListGroceries.as_view()),
	path('get-shop-fruits/<int:pk>', views.ListFruits.as_view()),
	path('get-shop-vegetables/<int:pk>', views.ListVegetables.as_view()),
	path('get-shop-slots/<int:pk>', views.ListVegetables.as_view()),

]