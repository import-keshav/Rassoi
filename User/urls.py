from django.urls import path

from . import views

urlpatterns = [
	path('register', views.RegisterUser.as_view()),
	path('login', views.LoginView.as_view()),

	path('check-mobile-number', views.CheckMobileNumber.as_view()),
	path('check-email', views.CheckEmail.as_view()),

	path('send-otp', views.SendOTP.as_view()),
	path('verify-otp', views.VerifyOTP.as_view()),

	path('change-user-password', views.ChangeUserPassword.as_view()),

	path('driver-login', views.DriverLogin.as_view()),

]