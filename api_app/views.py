from django.shortcuts import render
from rest_framework.views import APIView
from api_app.user_serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Organisation


class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            

            try:

                organisation = Organisation(
                    name = f"str({user.name}) + 's' + ' Organisation'",
                    description = ""
                )
                organisation.save()

            except Exception as e:
                return str(e)
            

            data = {
                        "status": "success",
                        "message": "Registration successful",
                        "data": {
                            "accessToken": access,
                            "user": {
                                "userId": user.userId,
                                "firstName": user.firstName,
                                "lastName": user.lastName,
                                "email": user.email,
                                "phone": user.email,
                                "password": user.password,
                            }
                        }
                    }
                          
        
            return Response(data, status.HTTP_201_CREATED)
        
        return Response({
                            "status": "Bad request",
                            "message": "Registration unsuccessful",
                            "statusCode": 400
                        }, status.HTTP_400_BAD_REQUEST)

        
