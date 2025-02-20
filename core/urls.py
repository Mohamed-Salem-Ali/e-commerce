from django.urls import include, path 
from . import views 

# URL patterns for the e-commerce application
urlpatterns = [
    path('',views.home,name="home"),                                                # Home page
    path('cart/',views.cart,name="cart"),                                           # Shopping cart page
    path('checkout/',views.checkout,name="checkout"),                               # Checkout page
    path('orders/', views.ordersPage, name="orders"),                               # Orders history page
    path('product/<int:product_id>/', views.product_detail, name='product_detail'), # Product detail page

    #API Endpoints
    path('update_item/', views.updateItem, name="update_item"),                     # API to update cart items
    path('process_order/', views.processOrder, name="process_order"),               # API for Process order after checkout
    
    # PayPal integration URLs
    path('paypal',include("paypal.standard.ipn.urls")),                         # PayPal IPN handling
    path('payment_success',views.payment_success,name='payment_success'),           # Successful payment page
    path('payment_failed',views.payment_failed,name='payment_failed')               # Failed payment page
]