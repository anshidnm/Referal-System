from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    referal_code = serializers.CharField(max_length=250, required=False)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "password",
            "referal_code"
        ]
    
    def validate(self, attrs):
        errors = {}
        if User.objects.filter(email__iexact=attrs["email"]).exists():
            errors["email"] = "This email already exist with another user"
        if (
            "referal_code" in attrs and
            not User.objects.filter(my_referal_code__iexact=attrs["referal_code"]).exists()
        ):
          errors["referal_code"] = "Invalid referal code"      
        if errors:
            raise serializers.ValidationError(errors)    
        return super().validate(attrs)
    
    def save(self, **kwargs):
        if "referal_code" in self.validated_data:
            referal_code = self.validated_data["referal_code"]
            referer = User.objects.filter(my_referal_code__iexact=referal_code)

        user = User.objects.create(
            name=self.validated_data["name"],
            email=self.validated_data["email"],
        )
        user.set_password(self.validated_data["password"])
        user.generate_referal_code()
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "password",
            "referal_code",
            "referal_points",
            "date_joined",
        ]
        read_only_fields = ["referal_code", "date_joined"]