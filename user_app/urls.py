from django.conf.urls import url
from django.urls import path
from user_app import views
from . import views
urlpatterns = [
    # 'path' works very well than 'url'
    # path('',views.index, name="index"),
    path('register/',views.register, name="register"),
    # path('webpage/',views.django_laveltwo, name="webpage"),
]