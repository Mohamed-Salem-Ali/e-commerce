from django.urls import include, path 
from . import views 
urlpatterns = [
    path('',views.home,name="home"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('orders/', views.ordersPage, name="orders"),
    path('process_order/', views.processOrder, name="process_order"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('paypal',include("paypal.standard.ipn.urls")),
    path('payment_success',views.payment_success,name='payment_success'),
    path('payment_failed',views.payment_failed,name='payment_failed')
]