from django.urls import path
from . import views

urlpatterns = [
    path('', views.apisOverview, name='apis-overview'),
    path('inventory-list', views.inventoryList, name='inventory-list'),
    path('inventory-detail/<str:pk>/', views.inventoryDetail, name='inventory-detail'),
    path('inventory-create', views.inventoryCreate, name='inventory-create'),
    path('inventory-update/<str:pk>/', views.inventoryUpdate, name='inventory-update'),
    path('inventory-delete/<str:pk>/', views.inventoryDelete, name='inventory-delete'),


]


