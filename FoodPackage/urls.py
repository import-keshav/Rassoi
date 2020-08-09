from django.urls import path

from . import views

urlpatterns = [
	path('get-client-food-package/<int:pk>', views.ListClientFoodPackage.as_view()),
	path('get-shop-food-package/<int:pk>', views.ListShopFoodPackage.as_view()),
	path('create-food-package', views.CreateFoodPackage.as_view()),
	path('add-dish-in-food-package', views.CreateFoodPackageMeal.as_view()),
	path('update-delete-food-package/<int:pk>', views.UpdateDeleteFoodPackage.as_view()),
	path('update-delete-food-package-meal/<int:pk>', views.UpdateDeleteFoodPackageMeal.as_view()),
]