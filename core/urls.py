from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Sillabuz Backend Imparable",
        default_version='v1',
        description="This a basic clone by deezer",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="yahyrparedesarteaga@gmail.com"),
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=False,
    permission_classes=[permissions.IsAuthenticated, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("apps.commons.api.urls")),
    path('api/', include("apps.clients.api.urls")),
    path('', include('rest_framework.urls')),
    re_path(r'^api(?P<format>\.json|\.yaml)$', login_required(schema_view.without_ui(cache_timeout=None))),
    re_path(r'^api/$', login_required(schema_view.with_ui('swagger', cache_timeout=None))),
    re_path(r'^docs/$', login_required(schema_view.with_ui('redoc', cache_timeout=None))),
    path('', lambda request: redirect('/api', permanent=False)),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
