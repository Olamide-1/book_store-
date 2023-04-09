from django.urls import path

from oauth2_provider.views import AuthorizationView, TokenView

from . import views

urlpatterns = [
    path("authorize/", AuthorizationView.as_view(), name="oauth-authoize"),
    path("login/", views.LoginOauthView.as_view(), name="oauth-login"),
    path("google-auth/", views.GoogleAuthView.as_view(), name="google-auth")
]
