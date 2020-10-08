from django.urls import path

from . import views

urlpatterns = [
	path('get-shop-driver/<int:pk>', views.ListDrivers.as_view()),
	path('get-specific-driver/<int:pk>', views.GetSpecificDriver.as_view()),

	path('get-driver-normal-orders/<int:pk>', views.GetTodaysOrders.as_view()),
	path('get-driver-food-package-orders/<int:pk>', views.GetTodaysFoodPackageOrders.as_view()),

	path('delivered-normal-order/<int:order_id>', views.DeliveredNormalOrder.as_view()),
	path('delivered-food-package-meal-order/<int:order_id>', views.DeliveredFoodPackageMealOrder.as_view())
]