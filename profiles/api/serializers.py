from rest_framework import serializers
from profiles.models import Business, Customer

class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model: Business
        fields = '__all__'
        
class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model: Customer
        fields = '__all__'
