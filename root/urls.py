from django.urls import path
from . import views

urlpatterns = [

    # home page
    path('', views.index, name='index'),

    # short url redirect
    path('<str:short_url>/', views.redirect_url, name='redirect'),
]