from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import AccountSerializer, LoginSerilizer, CreateAccountSerializer

class RegisterView(generics.CreateAPIView):

    serializer_class = CreateAccountSerializer

class AccountView(generics.RetrieveUpdateAPIView):

    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class LoginView(generics.GenericAPIView):

    serializer_class = LoginSerilizer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        response = {
            "token": str(token)
        }

        return Response(response, status=status.HTTP_200_OK)

class LogoutView(generics.DestroyAPIView):

    permission_classes = [IsAuthenticated]

    def get_object(self):

        return Token.objects.get(user=self.request.user)

