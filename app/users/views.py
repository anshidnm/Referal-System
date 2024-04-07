from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView, 
    GenericAPIView, 
    ListAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .schemas import Documentation
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer
)


@Documentation.REGISTER
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            ser = self.get_serializer(data=request.data)
            if ser.is_valid():
                user = ser.save()
                token = RefreshToken.for_user(user)
                return Response(
                    {
                        "user_id": user.id,
                        "message": "user registered successfully",
                        "refresh": str(token),
                        "access": str(token.access_token)
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {"message": "something went wrong"},
                status=status.HTTP_400_BAD_REQUEST
            )


@Documentation.LOGIN
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


@Documentation.MY_DETAILS
class UserDetailsView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        ser = self.get_serializer(user, many=False)
        return Response(ser.data)


@Documentation.REFERALS
class ReferalsView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(referals=self.request.user.id)
