from rest_framework import viewsets

from apps.commons.api.serializers import GenderSerializer, LanguageSerializer, CountrySerializer
from apps.commons.models import Gender, Country, Language


# Create your viewsets here.
class GenderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gender.objects.filter(is_active=True)
    serializer_class = GenderSerializer


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.filter(is_active=True)
    serializer_class = CountrySerializer


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.filter(is_active=True)
    serializer_class = LanguageSerializer
