from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from core.models import PorterProfile , FarmerProfile, MilkCollection
from rest_framework.response import Response
# Create your views here.
@api_view(['POST'])
@permission_classes( [IsAuthenticated])
def AddMilkCollection(request):
    # get the logged in user- porter
    try:
        porter=request.user.porter_profile
    except PorterProfile.DoesNotExist:
        return Response({"error":"Only porter can add milk collection"})
    
    # check if the farmer exists 
    try:
        national_id=request.data.get("national_id")
        farmer=FarmerProfile.objects.get(national_id=national_id)
    except FarmerProfile.DoesNotExist:
        return Response({"error":"farmer not found"})

    collection=MilkCollection.objects.create(
        farmer=farmer,
        porter=porter,
        litres=request.data.get("litres"),
        session=request.data.get("session")
    )
    return Response({
        "message":"Milk_collection recorded succesfully",
        "collection_id":collection.id,
        "farmer":f"{farmer.first_name} {farmer.last_name}",
        "porter":f"{porter.first_name} {porter.last_name}",
        "litres":collection.litres
    })