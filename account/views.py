from django.shortcuts import render
from .models import *
from . serializers import *
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .task import send_welcome_email
from rest_framework.response import Response


class CustomUserApiView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email.delay(user.email)
        return Response({'message': 'User registered successfully'}, status=201)


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)