from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('remove/<str:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<str:item_id>/', views.update_cart_item, name='update_cart_item'),

]

