#used to see our db tables from various views
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
#get data from drinks table
def drinksList(request):
    """
    Description
        - this function will get the drinks from our table in json format
    Args:
        - request: perform actions on drinks gotten
    Returns:
        - drinks in json format
    """
    #get drinks
    drinks = Drink.objects.all()
    #serialize them
    serializer = DrinkSerializer(drinks, many=True)
    #return json
    return JsonResponse({"drinks": serializer.data}, safe=False)
