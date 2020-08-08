from django.urls import path

from . import views

urlpatterns = [
	path('get-shop-groceries/<int:pk>', views.ListGroceries.as_view()),
	path('get-specific-shop-grocery/<int:pk>', views.ListSpecificGrocery.as_view()),
	path('create-groceries', views.CreateGrocery.as_view()),
	path('create-groceries-price', views.CreateGroceryPrice.as_view()),
	path('change-grocery-availability/<int:pk>', views.ChangeIsAvailibilityOfGrocery.as_view()),
]