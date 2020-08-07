from django.urls import path

from . import views

urlpatterns = [
	path('get-shop-vegetables/<int:pk>', views.ListVegetables.as_view()),
	path('get-specific-shop-vegetable/<int:pk>', views.ListSpecificVegetable.as_view()),
	path('create-vegetable', views.CreateVegetable.as_view()),
	path('create-vegetable-price', views.CreateVegetablePrice.as_view()),
	path('change-vegetable-availability', views.ChangeIsAvailibilityOfVegetable.as_view()),
]
