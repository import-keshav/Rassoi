from django.urls import path

from . import views

urlpatterns = [
	path('get-shop-feedback/<int:pk>', views.ListShopFeedBack.as_view()),
	path('create-feedback', views.CreateShopFeedBack.as_view()),
	path('update-delete-shop-feedback/<int:pk>', views.UpdateDeleteFeedBack.as_view()),
]