from django.shortcuts import render
from rest_framework.views import APIView
from api_app.api_serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)

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
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        
