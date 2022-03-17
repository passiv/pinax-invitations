from django.urls import include, path

urlpatterns = [
    path('account', include("account.urls")),
    path('', include("pinax.invitations.urls", namespace="pinax_invitations")),
]
