"""rassoi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('approval/', include('Approval.urls')),
    path('cart/', include('Cart.urls')),
    path('client/', include('Client.urls')),
    path('driver/', include('Driver.urls')),
    path('feedback/', include('Feedback.urls')),
    path('food/', include('Food.urls')),
    path('food-package/', include('FoodPackage.urls')),
    path('fruit/', include('Fruit.urls')),
    path('grocery/', include('Grocery.urls')),
    path('order/', include('Order.urls')),
    path('promocode/', include('Promocode.urls')),
    path('shop/', include('Shop.urls')),
    path('vegetable/', include('Vegetable.urls')),
    path('user/', include('User.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Ras'soi Admin Panel"
admin.site.site_title = "Ras'soi"