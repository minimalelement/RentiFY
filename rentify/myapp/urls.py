from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview, name="home"),

    path('services',views.servicepage, name="servicepage"),

    path('about',views.aboutuspage, name="aboutuspage"),
]
