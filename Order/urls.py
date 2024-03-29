from django.urls import path

from . import views

urlpatterns = [
	path('create-order', views.CreateOrder.as_view()),
	path('update-order/<int:pk>', views.UpdateOrder.as_view()),
	path('order-completed',  views.OrderCompleted.as_view()),

	path('get-shop-ongoing-orders/<int:pk>', views.ListOngoingShopOrder.as_view()),
	path('get-shop-past-order/<int:pk>', views.ListShopPastOrder.as_view()),
	path('get-specific-shop-ongoing-order/<int:pk>', views.ListSpecificOngoingShopOrder.as_view()),
	path('get-specific-shop-order/<int:pk>', views.ListSpecificShopOrder.as_view()),

	path('get-client-ongoing-order/<int:pk>', views.ListClientOngoingOrder.as_view()),
	path('get-client-past-order/<int:pk>', views.ListClientPastOrder.as_view()),

	path('get-today-package-order/<str:type>/<str:date>/<int:shop_id>',  views.GetTodayFoodPackageOrder.as_view()),
	path('get-client-package-order/<str:date>/<int:client_id>',  views.GetClientPackageOrder.as_view()),
	path('update-daily-food-package-order/<int:pk>',  views.UpdateClientDailyPackageOrder.as_view())
]