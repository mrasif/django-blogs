from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer



User = get_user_model()

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        if serializer.is_valid():
            data = serializer.data
            print(data)
            user = User.objects.filter(email=data['email'])
            if user:
                user=user.first()
                authenticated_user = user.check_password(data['password'])
                if authenticated_user:
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({'token':token.key}, status=status.HTTP_200_OK)
                else:
                    return Response({'error':'Invalid password!'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error':'User not registered!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            # return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'Bad request!'}, status=status.HTTP_400_BAD_REQUEST)