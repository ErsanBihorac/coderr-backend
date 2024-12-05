from django.contrib.auth.models import User
from rest_framework import serializers
from authentication.api.utils import create_user, create_business_or_customer

class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)
    type = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password', 'type']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def save(self):
        account = create_user(self.validated_data['username'],
                              self.validated_data['email'],
                              self.validated_data['password'],
                              self.validated_data['repeated_password'])
        
        create_business_or_customer(self.validated_data['type'], account)
        return account