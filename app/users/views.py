from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            ser = self.get_serializer(data=request.data)
            if ser.is_valid():
                user = ser.save()
                return Response(
                    {
                        "user_id": user.id,
                        "message": "user registered successfully"
                    }
                )
            else:
                return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {"message": "something went wrong"},
                status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        try:
            ser = self.get_serializer(data=request.data)
            if ser.is_valid():
                user = authenticate(
                    email=ser.validated_data["email"],
                    password=ser.validated_data["password"]
                )
                if user is not None:
                    token = RefreshToken.for_user(user)
                    res = {
                        "refresh": str(token),
                        "access": str(token.access_token)
                    }
                    return Response(res)
                return Response(
                    {"message": "Invalid credentials"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {"message": "something went wrong"},
                status=status.HTTP_400_BAD_REQUEST
            )

