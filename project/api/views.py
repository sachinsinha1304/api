from django.shortcuts import render
from django.http.response import JsonResponse
from .models import item,userDetails,Biddings,SoldItems
from .serializers import itemSerializer,userSerializer,biddSerializer
from rest_framework import viewsets
from chatbot import main

from datetime import date

from datetime import date

# Create your views here.

class itemViewSet(viewsets.ModelViewSet):
    queryset = item.objects.all()
    serializer_class = itemSerializer

class userViewSet(viewsets.ModelViewSet):
    queryset = userDetails.objects.all()
    serializer_class = userSerializer

class biddViewSet(viewsets.ModelViewSet):
    queryset = Biddings.objects.all()
    serializer_class = biddSerializer


def chatBot(request, var):
    return JsonResponse({"bot":main.get_response(var)})

def my(request):
    day = date.today()
    data = item.objects.filter(closingDate = day)
    for i in data:

        # getting the object with greatest bid
        obj = Biddings.objects.filter(itemId = i.id).order_by("-bidd")[:1]

        # now storing the data in SoldItems table
        for val in obj:
            pr = val.bidd
            cust_id = val.custId

        s = SoldItems(itemId = i.id, custId = cust_id, price = pr)
        s.save()

        # changing status of item as sold
        file = item.objects.get(id = i)
        file.status = True
        file.save()

        # to removing the bids made on said item
        Biddings.objects.filter(itemId = i.id).delete()

    return JsonResponse({"bot":"done"})


    

