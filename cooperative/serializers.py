from rest_framework import serializers

from core.models import FarmerProfile, PorterProfile

# admin/cooperative farmer account 
class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model=FarmerProfile
        fields='__all__'

class PorterSerializer(serializers.ModelSerializer):
    class Meta:
        model=PorterProfile
        fields='__all__'

        