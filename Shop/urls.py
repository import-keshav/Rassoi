from django.urls import path

from . import views

urlpatterns = [
	path('get-specific-shop/<int:pk>', views.ListSpecificShop.as_view()),
	path('shop-login', views.ShopLogin.as_view()),

	path('get-shop-groceries/<int:pk>', views.ListGroceries.as_view()),
	path('get-specific-shop-grocery/<int:pk>', views.ListSpecificGrocery.as_view()),
	path('create-groceries', views.CreateGrocery.as_view()),
	path('create-groceries-price-in-kg', views.CreateGroceryInKgQuantityPrice.as_view()),
	path('create-groceries-price-in-num', views.CreateGroceryInNumOfItemsPrice.as_view()),
	path('create-groceries-price-in-lts', views.CreateGroceryInLitresPrice.as_view()),

	path('get-shop-fruits/<int:pk>', views.ListFruits.as_view()),
	path('get-specific-shop-fruit/<int:pk>', views.ListSpecificFruit.as_view()),
	path('create-fruit', views.CreateFruit.as_view()),

	path('get-shop-vegetables/<int:pk>', views.ListVegetables.as_view()),
	path('get-specific-shop-vegetable/<int:pk>', views.ListSpecificVegetable.as_view()),
	path('create-vegetable', views.CreateVegetable.as_view()),

	path('get-shop-slots/<int:pk>', views.ListSlots.as_view()),
	path('create-shop-slot', views.CreateSlot.as_view()),
	path('update-delete-shop-slot/<int:pk>', views.UpdateDeleteSlot.as_view()),

	path('get-shop-packages/<int:pk>', views.ListFoodPackages.as_view()),
	path('get-specific-shop-package/<int:pk>', views.ListSpecificFoodPackage.as_view()),
	path('create-food-package', views.CreateFoodPackage.as_view()),

	path('get-food-meal/<int:pk>', views.ListFoodMeal.as_view()),
	path('get-specific-food-meal/<int:pk>', views.ListFoodMeal.as_view()),
	path('create-food-meal', views.CreateFoodMeal.as_view()),
	path('create-food-dish', views.CreateFoodDish.as_view()),

	path('get-shop-promocode/<int:pk>', views.ListShopPromocode.as_view()),
	path('create-promocode', views.CreateShopPromocode.as_view()),
	path('update-delete-shop-promocode/<int:pk>', views.UpdateDeleteShopPromocode.as_view()),

]