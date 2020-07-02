from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),        
    path('thanks/', views.thanks, name='thanks'),
    path('checkout/', views.checkout, name='checkout'),        
]
