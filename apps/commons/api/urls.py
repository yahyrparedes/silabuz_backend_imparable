from django.urls import path, include
from rest_framework import routers

from apps.commons.api.viewsets import GenderViewSet, LanguageViewSet, CountryViewSet

router = routers.DefaultRouter()
router.register('genders', GenderViewSet)
router.register('countries', CountryViewSet)
router.register('languages', LanguageViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
