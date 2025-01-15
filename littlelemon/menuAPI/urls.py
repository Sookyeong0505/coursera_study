from django.urls import path
from . import views

urlpatterns = [
    # path('', views.menu, name='menu'),
    path('menus/', views.MenuList.as_view()),
    path('menus/<int:pk>', views.Menu.as_view()),
]