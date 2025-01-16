from django.urls import path
from . import views

urlpatterns = [
    path('menu', views.menu_items),
    path('menu/<int:id>', views.single_item),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemsView.as_view()),
    path('category/', views.CategoryView.as_view()),
]