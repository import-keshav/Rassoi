from django.urls import path

from . import views

urlpatterns = [
	path('get-shop-driver/<int:pk>', views.ListDrivers.as_view()),
]