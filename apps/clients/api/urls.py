from django.urls import path

from apps.clients.api.views import SignUpClientApiView, SignInClientApiView, ClientProfileView

urlpatterns = [
    path('v1/clients/signup', SignUpClientApiView.as_view()),
    path('v1/clients/signin', SignInClientApiView.as_view()),
    path('v1/clients/profile', ClientProfileView.as_view()),
]
