#used to see our db tables from various views
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#CRUD operations
@api_view(['GET', 'POST'])
#get data from drinks table
def drinksList(request):
    """
    Description
        - this function will get the drinks from our table in json format
    Args:
        - request: perform CRUD actions on drinks gotten
    Returns:
        - drinks in json format
        - updates drinks
        - posts a new drink
        - deletes a drink
    """
    if request.method == 'GET':
        #get drinks
        drinks = Drink.objects.all()
        #serialize them
        serializer = DrinkSerializer(drinks, many=True)
        #return json
        return JsonResponse({"drinks": serializer.data})
    #POST
    #used to validate if a new file is created
    if request.method == 'POST':
        serializer = DrinkSerializer(data = request.data)
        #if we have created the right data a new drink will be created
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
#drink details get 1 drink, delete one drink, update a drink
@api_view(['GET','PUT','DELETE'])
def drinkDetails(request, id):
    """
    Description:
         - this function will perfrom CRUD operations on 1 drink
    Args:
        - request: parameter used to interact with drink data
    Returns:
        - CRUD operation
    """
    #get a drink by its id if found
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #get one drink
    if request.method == "GET":
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    #PUT update
    elif request.method == 'PUT':
        pass
    #delete
    elif request.method == "DELETE":
        pass
    
