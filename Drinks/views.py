from django.shortcuts import render

from .models import Drinks
from .serializers import DrinksSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here


def home(request):
    return render(request,'Drinks/index.html')

# implementing the API for the drinks app
# get
@api_view(['GET'])
def get_drinks(request):
    if request.method == 'GET':
        drinks = Drinks.objects.all() # all abojects[]
        ds= DrinksSerializer(drinks, many=True) 
        return Response(ds.data)
    
#get specific drink
@api_view(['GET'])
def get_drink(request, id):
    if request.method == 'GET': #
        drink = Drinks.objects.get(id=id) # all abojects[]
        ds= DrinksSerializer(drink, many=False) 
        return Response(ds.data)

# put method Update the drink
@api_view(['PUT'])
def update_drink(request, id):
    if request.method == 'PUT':
        data = request.data
        drink = Drinks.objects.get(id=id) # all abojects[]
        ds= DrinksSerializer(instance=drink, data=request.data) 
        if ds.is_valid():
            ds.save()
            return Response(ds.data, status=200)
        return Response(ds.errors, status=400)

#delete method
@api_view(['DELETE'])
def delete_drink(request, id):
    if request.method == 'DELETE':
        drink = Drinks.objects.get(id=id) # all abojects[]
        drink.delete()
        return Response(status=204)


# post method
@api_view(['POST'])
def add_drink(request):
    if request.method == 'POST':
        data = request.data
        ds = DrinksSerializer(data=request.data)
        if ds.is_valid():
            ds.save()
            return Response(ds.data, status=201)
        return Response(ds.errors, status=400) 
