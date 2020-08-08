from django.urls import path

from . import views

urlpatterns = [
	path('get-food-meal/<int:pk>', views.ListFoodMeal.as_view()),
	path('get-specific-food-meal/<int:pk>', views.ListFoodMeal.as_view()),
	path('create-food-meal', views.CreateFoodMeal.as_view()),
	path('create-food-dish', views.CreateFoodDish.as_view()),
	path('change-food-meal-availability/<int:pk>', views.ChangeIsAvailibilityOfFoodMeal.as_view()),
]
