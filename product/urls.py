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
from product import views
urlpatterns = [
   
   path('addproduct',views.add),
   path('delete/<int:id>',views.delete),
   path('update/<int:id>',views.update),

    path('add-to-cart/<int:id>/<int:uid>',views.addtocart),
    path('buyproduct/<int:id>/<int:uid>',views.buy),

    path('cart_delete/<int:id>/<int:uid>',views.deletecart),

    path('delivered/<int:id>/<int:uid>',views.delivered),






    
]