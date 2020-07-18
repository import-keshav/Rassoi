from django.urls import path

from . import views

urlpatterns = [
	path('get-client-info/<int:pk>', views.GetClientInfo.as_view()),
	path('get-client-notification/<int:pk>', views.ListClientNotification.as_view()),

	path('get-client-fruit-cart/<int:pk>', views.ListItemInClientFruitCart.as_view()),
	path('add-fruit-in-client-fruit-cart', views.AddItemInClientFruitCart.as_view()),
	path('update-delete-client-fruit-cart/<int:pk>', views.UpdateDeleteItemInClientFruitCart.as_view()),

	path('get-shop-feedback/<int:pk>', views.ListShopFeedBack.as_view()),
	path('create-feedback', views.CreateShopFeedBack.as_view()),
	path('update-delete-shop-feedback/<int:pk>', views.UpdateDeleteFeedBack.as_view()),

]