from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InventorySerializer, WarehouseSerializer

from .models import Inventory, Warehouse
# Create your views here.

@api_view(['GET'])
def apisOverview(request):
	api_urls = {
		'List':'/Inventory-list/',
		'Detail View':'/Inventory-detail/<str:pk>/',
		'Create':'/Inventory-create/',
		'Update':'/Inventory-update/<str:pk>/',
		'Delete':'/Inventory-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def inventoryList(request):
	inventorys = Inventory.objects.all().order_by('-id')
	serializer = InventorySerializer(inventorys, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def inventoryDetail(request, pk):
	inventorys = Inventory.objects.get(id=pk)
	serializer = InventorySerializer(inventorys, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def inventoryCreate(request):
	serializer = InventorySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def inventoryUpdate(request, pk):
	inventory = Inventory.objects.get(id=pk)
	serializer = InventorySerializer(instance=inventory, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def inventoryDelete(request, pk):
	inventory = Inventory.objects.get(id=pk)
	inventory.delete()

	return Response('Inventory succsesfully delete!')


