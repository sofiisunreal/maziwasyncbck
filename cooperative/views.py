from django.shortcuts import render
from numpy import generic
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser

from core.models import FarmerProfile, MilkCollection, Notice, PorterProfile, Feedback
from collector.serializers import MilkCollectionSerializer
from farmer.serializers import FeedbackSerializer
from  .serializers import FarmerSerializer, NoticeSerializer, PorterSerializer
# Create your views here.

# view farmer feedback
class ViewFeedback(generics.ListAPIView):
    serializer_class=FeedbackSerializer
    permission_classes=[IsAdminUser]
     
    def get_queryset(self):
        feedback=Feedback.objects.order_by('created_at')
        return feedback


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



    
# notices board 
class NoticeViewSet(viewsets.ModelViewSet):
    queryset=Notice.objects.all()
    serializer_class=NoticeSerializer
    permission_classes=[IsAdminUser]

    def perform_create(self, serializer):
       serializer.save(created_by=self.request.user)