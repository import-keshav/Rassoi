from django.urls import path

from . import views

urlpatterns = [
	path('get-shop-vegetables/<int:pk>', views.ListVegetables.as_view()),
	path('get-client-side-vegetables/<int:shop>/<int:client>', views.ListVegetablesOnClientSide.as_view()),
	path('get-specific-shop-vegetable/<int:pk>', views.ListSpecificVegetable.as_view()),
	path('create-vegetable', views.CreateVegetable.as_view()),
	path('create-vegetable-price', views.CreateVegetablePrice.as_view()),
	path('change-vegetable-availability/<int:pk>', views.ChangeIsAvailibilityOfVegetable.as_view()),
]
