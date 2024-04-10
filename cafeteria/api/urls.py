from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.items, name='items'),
    path('items/<int:pk>/', views.item, name='item'),
    path('item_create/', views.item_create, name='item_create'),
    path('item_update/<int:pk>/', views.item_update, name='item_update'),
    path('item_delete/<int:pk>/', views.item_delete, name='item_delete')
]
