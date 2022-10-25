from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.clients.models import Client
from apps.commons.api.serializers import LanguageSerializer, GenderSerializer
from apps.users.models import User


class SignUpClientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, max_length=254,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    firstname = serializers.CharField(required=True, max_length=254, )
    lastname = serializers.CharField(required=False, max_length=254, )
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
    )
    confirm = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
    )

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def to_representation(self, instance):
        instance.email = instance.user.email
        instance.firstname = instance.user.first_name
        instance.lastname = instance.user.last_name
        return super(SignUpClientSerializer, self).to_representation(instance)

    class Meta:
        model = Client
        fields = ['email', 'firstname', 'lastname', 'password', 'confirm',
                  'gender', 'country', 'lang', 'tracklist', 'date_of_birth', 'link', 'is_kid']


class ClientPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    firstname = serializers.CharField(source='user.first_name')
    lastname = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    gender = GenderSerializer()
    lang = LanguageSerializer()
    inscription_date = serializers.DateTimeField(source='created_at')

    class Meta:
        model = Client
        fields = [
            'username', 'firstname', 'lastname', 'email',
            'date_of_birth',
            'inscription_date',
            'gender',
            'link',
            'picture',
            'country',
            'lang',
            'is_kid',
            'tracklist',
            'is_active',
        ]
