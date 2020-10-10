from django.urls import path

from . import views

urlpatterns = [
	path('get-specific-shop/<int:pk>', views.ListSpecificShop.as_view()),
	path('shop-login', views.ShopLogin.as_view()),

	path('get-shop-slots/<int:pk>', views.ListSlots.as_view()),
	path('create-shop-slot', views.CreateSlot.as_view()),
	path('update-delete-shop-slot/<int:pk>', views.UpdateDeleteSlot.as_view()),

	path('get-nearest-shop', views.GetNearestShop.as_view()),

]