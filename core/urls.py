from django.urls import path 
from . import views 
urlpatterns = [
    path('',views.home,name="home"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('orders/', views.ordersPage, name="orders"),
    path('process_order/', views.processOrder, name="process_order"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
