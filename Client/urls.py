from django.urls import path

from . import views

urlpatterns = [
	path('get-client-info/<int:pk>', views.GetClientInfo.as_view()),
	path('get-client-notification/<int:pk>', views.ListClientNotification.as_view()),
]