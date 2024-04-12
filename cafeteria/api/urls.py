from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.items, name='items'),
    path('items/<int:pk>/', views.item, name='item'),
    path('item_create/', views.item_create, name='item_create'),
    path('item_update/<int:pk>/', views.item_update, name='item_update'),
    path('item_delete/<int:pk>/', views.item_delete, name='item_delete'),
    path('categories/', views.categories, name='categories'),
    path('category_create/', views.category_create, name="category_create"),
    path('category_delete/<int:pk>/', views.category_delete, name="category_delete")
]
