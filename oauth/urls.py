from django.urls import path

from oauth2_provider.views import AuthorizationView, TokenView

from . import views

urlpatterns = [
    path("authorize/", AuthorizationView.as_view(), name="oauth-authoize"),
    path("token/", TokenView.as_view(), name="oauth-token"),
    path("userinfo/", views.UserInfoView.as_view(), name="oauth-userinfo"),
    path("login/", views.LoginOauthView.as_view(), name="oauth-login"),
    path("wallet-payment/", views.WalletAuthView.as_view(), name="walletauth"),
    path("google-auth/", views.GoogleAuthView.as_view(), name="google-auth")
]
