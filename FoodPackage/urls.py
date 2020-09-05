from django.urls import path

from . import views

urlpatterns = [
	path('create-food-package', views.CreateFoodPackage.as_view()),
	path('get-client-food-package/<int:pk>', views.ListClientFoodPackage.as_view()),
	path('get-food-package-on-day/<str:day>/<str:type>', views.GetFoodPackageOnDay.as_view())
]