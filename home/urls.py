from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='index' ),
    path('about/',about_us, name='about_us'),
    path('contact/',contact_us, name='contact_us'),
    path('login/',customer_login, name='customer_login'),
    path('signup/',customer_signup, name='customer_signup'),
    path('products/',products,name='products'),
    path('product-details/',product_details,name='product_details'),
    path('shopping-cart/',shopping_cart,name='shopping_cart'),
    path('blog/',blog,name='blog'),
    path('blog-details/',blog_details,name='blog_details'),
    path('cart/', cart,name='cart' ),
]