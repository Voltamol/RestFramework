from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, World!"})

@api_view(['POST'])
def create_item(request):
    # Logic to create a new item
    return Response({"message": "Item created"})

@api_view(['PUT'])
def update_item(request, item_id):
    # Logic to update an existing item with ID `item_id`
    return Response({"message": f"Item {item_id} updated"})

@api_view(['DELETE'])
def delete_item(request, item_id):
    # Logic to delete an existing item with ID `item_id`
    return Response({"message": f"Item {item_id} deleted"})