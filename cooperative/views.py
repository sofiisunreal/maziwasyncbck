from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from core.models import FarmerProfile, MilkCollection, PorterProfile
from collector.serializers import MilkCollectionSerializer
from  .serializers import FarmerSerializer, PorterSerializer
# Create your views here.

class FarmerViewSet(viewsets.ModelViewSet):
    queryset=FarmerProfile.objects.all()
    serializer_class=FarmerSerializer
    permission_classes=[IsAdminUser]
    http_method_names=['get','put','patch','delete']

class PorterViewSet(viewsets.ModelViewSet):
    queryset=PorterProfile.objects.all()
    serializer_class=PorterSerializer
    permission_classes=[IsAdminUser]
    http_method_names=['get','put','patch','delete']

class MilkCollectionViewSet(viewsets.ModelViewSet):
    queryset=MilkCollection.objects.select_related(
        'farmer',
        'porter'
    )
    serializer_class=MilkCollectionSerializer
    permission_classes=[IsAdminUser]
    http_method_names=['get','put','patch','delete']

    
