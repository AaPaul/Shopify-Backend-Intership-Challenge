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



    path('warehouse-list', views.warehouseList, name='warehouse-list'),
    path('warehouse-detail/<str:pk>/', views.warehouseDetail, name='warehouse-detail'),
    path('warehouse-create', views.warehouseCreate, name='warehouse-create'),
    path('warehouse-update/<str:pk>/', views.warehouseUpdate, name='warehouse-update'),
    path('warehouse-delete/<str:pk>/', views.warehouseDelete, name='warehouse-delete'),

@api_view(['GET'])
def warehouseList(request):
	WarehouseS = Warehouse.objects.all().order_by('-id')
	serializer = WarehouseSerializer(WarehouseS, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def warehouseDetail(request, pk):
	WarehouseS = Warehouse.objects.get(id=pk)
	serializer = WarehouseSerializer(WarehouseS, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def warehouseCreate(request):
	serializer = WarehouseSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def warehouseUpdate(request, pk):
	warehouse = Warehouse.objects.get(id=pk)
	serializer = WarehouseSerializer(instance=warehouse, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def warehouseDelete(request, pk):
	warehouse = Warehouse.objects.get(id=pk)
	warehouse.delete()

	return Response('Warehouse succsesfully delete!')