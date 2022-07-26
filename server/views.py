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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
