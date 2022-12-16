from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('index.html', views.index, name='index'),
path('about_us.html', views.about_us, name='about_us'),
path('cart.html', views.cart, name='cart'),
path('customer_service.html', views.customer_service, name='customer_service'),
path('equipment_accessories.html', views.equipment_accessories, name='equipment_accessories'),
path('instruments.html', views.instruments, name='instruments'),
path('product1.html', views.product1, name='product1'),
path('register.html', views.register, name='register'),
path('sign_in.html', views.sign_in, name='sign_in'),
]