from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexPage'),
    path('about/', views.about, name='aboutPage'),
    path('contact/', views.contact, name='contactPage'),
    path('products/', views.products, name='productsPage'),
    path('product-details/<slug:slug>/', views.products_detail, name='productDetailPage'),
    path('terms-and-conditions/', views.termandcondition, name='termandconditionPage'),
    path('cancellation-and-refund/', views.cancellationandrefund, name='cancellationandrefundPage'),
    path('privacy-and-policy/', views.privacyandpolicy, name='privacyandpolicyPage'),
    path('shipping-and-delivery/', views.shippinganddelivery, name='shippinganddeliveryPage'),
]