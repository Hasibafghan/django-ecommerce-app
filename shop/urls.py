from django.urls import path
from . import views

urlpatterns = [
    path('' , views.products , name='products'),
    path('about/' , views.about_us , name='about'),
    path('login/' , views.login_user , name='login'),
    path('logout/' , views.logout_user , name='logout'),
]
