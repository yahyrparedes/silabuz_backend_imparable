# Django Rest Framework
from rest_framework import serializers

from apps.commons.models import Gender, Country, Language


class GenderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Gender
        fields = ['id', 'short_name', 'long_name']


class CountrySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Country
        fields = [
            'id',
            'name',
            'alpha2code',
            'phone_prefix',
        ]


class LanguageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Language
        fields = [
            'id',
            'name',
            'code',
        ]
