from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'firstName':  {'required': False},
            'lastName': {'required': False},
            'email': {'required': False},
            'password': {'required': False}
        }

    def validate(self, attrs):

        errors = []

        if not attrs.get('firstName'):
            data = {
                "field": "firstName",
                "message": "firstName must not be null"  
            }
            errors.append(data)

        if not attrs.get('lastName'):
            data = {
                "field": "lastName",
                "message": "lastName must not be null"
            }
            errors.append(data) 

        if not attrs.get('email'):
            data = {
                "field": "email",
                "message": "email must not be null"
            }
            errors.append(data)
        if User.objects.filter(email=attrs.get('email')):
            data = {
                "field": "email",
                "message": "email already exists"
            } 
        
        if not attrs.get('password'):
            data = {
                "field": "password",
                "message": "password must not be null"
            }
            errors.append(data) 
        
        if errors:
            raise serializers.ValidationError({
                'errors': errors
            })
        
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(firstName=validated_data['firstName'], lastName=validated_data['lastName'],\
                                email=validated_data['email'], password=validated_data['password'])
    
        user.save()

        return user

