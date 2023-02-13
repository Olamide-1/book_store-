from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()

class CreateAccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password"
        ]
    
    def __init__(self, instance=None, **kwargs):
        super().__init__(instance, **kwargs)

        self.fields["id"].read_only = True
        self.fields["password"].write_only = True
    
    def validate(self, attrs):
        validate_password(attrs["password"])

        return attrs

    def create(self, validated_data):

        return self.Meta.model.objects.create_user(**validated_data)
    

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        ]

    def validate(self, attrs):
        return attrs

    def update(self, instance, validated_data):

        for attrs, value in validated_data.items():
            setattr(instance, attrs, value)

        instance.save()

        return instance
    


class LoginSerilizer(serializers.Serializer):

    username = serializers.CharField(max_length=60, required=True)
    password = serializers.CharField(max_length=60, required=True)

    def validate(self, attrs):
        
        user = authenticate(username=attrs["username"], password=attrs["password"])

        if not user:
            raise serializers.ValidationError("invalid Credentials")

        attrs["user"] = user

        return attrs