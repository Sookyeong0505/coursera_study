from django.urls import path
from . import views

urlpatterns = [
    # path('', views.menu, name='menu'),
    path('', views.MenuList.as_view(), name='menu'),
]