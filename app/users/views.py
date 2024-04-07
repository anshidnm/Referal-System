from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
\
from .models import User
from .serializers import RegisterSerializer


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
            pass
        return super().create(request, *args, **kwargs)