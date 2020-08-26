from django.urls import path

from . import views

urlpatterns = [
	path('create-order', views.CreateOrder.as_view()),
	path('get-shop-ongoing-orders/<int:pk>', views.ListOngoingShopOrder.as_view()),
	path('get-specific-shop-ongoing-order/<int:pk>', views.ListSpecificOngoingShopOrder.as_view()),
]