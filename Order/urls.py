from django.urls import path

from . import views

urlpatterns = [
	path('create-order', views.CreateOrder.as_view()),
]