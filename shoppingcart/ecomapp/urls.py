from django.urls import path
from .views import *

app_name='ecomapp'
urlpatterns = [
    path("",Homeview.as_view(),name="home"),
    path("about/",Aboutview.as_view(),name="about"),
    path("contactus/",Contactview.as_view(),name="contact"),
    path("allproducts/",Allproductsview.as_view(),name='allproducts'),
    path("product/<slug:slug>/",Productdetailview.as_view(),name="productdetail"),
    
    path("addtocart<int:pro_id>/",Addtocartview.as_view(),name="addtocart"),
    path("mycart/",Mycartview.as_view(),name="mycart"),
    path("managecart/<int:cp_id>/",Managecartview.as_view(),name="managecart"),
    path("emptycart/",Emptycartview.as_view(),name="emptycart"),
    
    path("checkout/",Checkoutview.as_view(),name="checkout"),
    path('register/',Customerregistrationview.as_view(),name="customerregistration"),
    path('logout/',Customerlogoutview.as_view(),name="customerlogout"),
    path('login/',Customerloginview.as_view(),name="customerlogin"),
    
    path("profile/",Customerprofileview.as_view(),name="customerprofile"),
    path("profile/order-<int:pk>/",Customerorderdetailview.as_view(),name="customerorderdetail")
  
]