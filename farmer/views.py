from django.shortcuts import render
from core.models import FarmerProfile, Feedback, MilkCollection
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from collector.serializers import MilkCollectionSerializer
from farmer.serializers import FeedbackSerializer

# Create your views here.
# farmers milk collection 
class FarmerCollection(generics.ListAPIView):
    serializer_class=MilkCollectionSerializer
    permission_classes=[IsAuthenticated]

    # queryset- we fetch data from the model in a class
    def get_queryset(self):
        try:
            farmer=self.request.user.farmer_profile
        except FarmerProfile.DoesNotExist:
            raise PermissionDenied(
                "Only farmers can access this endpoint"
            )
        collections=MilkCollection.objects.filter(farmer=farmer).select_related("porter").order_by("created_at")

        return collections
    
# feedback CRUD- viewsets
class FeeedbackViewset(viewsets.ModelViewSet):
    serializer_class=FeedbackSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        try:
            farmer= self.request.user.farmer_profile
        except:
            raise PermissionDenied("Only farmers can access this endpoint")
        feedback=(
            Feedback.objects
            .filter(farmer=farmer)
            .order_by('created_at')
        )
        return feedback
    
    # post by the farmer token
    def perform_create(self,serializer):
        try:
            farmer=self.request.user.farmer_profile
        except:
            raise PermissionDenied("Only farmers can create feedback")
        
        serializer.save(farmer=farmer)