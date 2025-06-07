from django.urls import path
from . import views
from . import forms
urlpatterns = [
    path('' , views.products , name='products'),
    path('search/' , views.search_product , name='search'),
    path('about/' , views.about_us , name='about'),
    path('login/' , views.login_user , name='login'),
    path('logout/' , views.logout_user , name='logout'),
    path('signup/' , views.signup_user , name='signup'),
    path('update_user/' , views.update_user , name='update_user'),
    path('update_info/' , views.update_info , name='update_info'),
    path('change_password/' , views.update_password , name='change_password'),
    path('detail/<int:pk>/' , views.product_detail , name='detail'),
    path('category/<str:category_name>/' , views.category_products , name='category'),
    path('category/' , views.category_view , name='category_view'),
]
