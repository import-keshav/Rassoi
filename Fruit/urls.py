from django.urls import path

from . import views

urlpatterns = [
	path('get-shop-fruits/<int:pk>', views.ListFruits.as_view()),
	path('get-client-side-fruits/<int:shop>/<int:client>', views.ListFruitsOnClientSide.as_view()),
	path('get-specific-shop-fruit/<int:pk>', views.ListSpecificFruit.as_view()),
	path('create-fruit', views.CreateFruit.as_view()),
	path('create-fruit-price', views.CreateFruitPrice.as_view()),
	path('change-fruit-availability/<int:pk>', views.ChangeIsAvailibilityOfFruit.as_view()),
]
