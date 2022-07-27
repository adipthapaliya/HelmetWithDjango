"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from mainuser import views
urlpatterns = [
    

    path('',views.index),

    path('addproduct/',views.addproduct),
    path('editproduct/<int:id>',views.editproduct),


    path('shop',views.nike),
    path('shop/nike',views.nike),
    path('shop/adidas',views.adidas),
    path('shop/converse',views.converse),
    path('shop/puma',views.puma),

    path('order',views.order),

    path('message',views.message),





    path('login/',views.login),
    path('login/verification',views.verification),
    path('logout/',views.log_out),








    
]