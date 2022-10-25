from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.commons.models import Country, Gender, Language
from apps.users.api.serializers import AuthTokenSerializer

from apps.clients.models import Client
from apps.clients.api.serializers import ClientPublicSerializer, SignUpClientSerializer

from apps.users.models import User


class SignInClientApiView(APIView):
    serializer_class = AuthTokenSerializer
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            client_serializer = ClientPublicSerializer(user.client).data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'user': client_serializer, 'token': token.key})
        except Client.DoesNotExist:
            raise PermissionDenied


class SignUpClientApiView(CreateAPIView):
    queryset = Client.objects.none()
    permission_classes = (AllowAny,)
    serializer_class = SignUpClientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        patient = self.create_client(validated_data)
        return self.login_and_response(patient)

    def login_and_response(self, client):
        client_data = ClientPublicSerializer(
            instance=client, context={'user': client.user}
        ).data
        token, _ = Token.objects.get_or_create(user=client.user)
        return Response(
            {'token': token.key, 'user': client_data},
            status=status.HTTP_201_CREATED
        )

    def create_client(self, data):
        print(data)
        data.pop('confirm')
        user_data = {
            'email': data.pop('email'),
            'password': data.pop('password'),
            'first_name': data.pop('firstname'),
            'last_name': data.pop('lastname', '')
        }

        user = User.objects.create_user(**user_data)
        client = Client.objects.create(user=user, is_active=True, **data)

        return client


class ClientProfileView(RetrieveUpdateAPIView):
    model = Client
    serializer_class = ClientPublicSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, *args, **kwargs):
        return self.request.user.client
