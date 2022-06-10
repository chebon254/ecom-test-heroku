from django.urls import path

from .views import *
# URL Patterns
urlpatterns = [
    path('', store, name="store"), 
    path('checkout/', checkout, name="checkout"), 
    path('cart/', cart, name="cart"), 
    path('update_item/', updateItem, name="update_item"), 
    path('process_order/', processOrder, name="process_order"), 
    path('product_info/<int:pk>/', product_info, name="product_info")
]
