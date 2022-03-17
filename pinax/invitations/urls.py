from django.urls import path

from .views import (
    AddToAllView,
    AddToUserView,
    InviteStatView,
    InviteView,
    TopOffAllView,
    TopOffUserView,
)

app_name = "pinax_invitations"

urlpatterns = [
    path('invite/', InviteView.as_view(), name="invite"),
    path('invite-stat/<int:pk>/', InviteStatView.as_view(), name="invite_stat"),
    path('topoff/', TopOffAllView.as_view(), name="topoff_all"),
    path('topoff/<int:pk>/', TopOffUserView.as_view(), name="topoff_user"),
    path('addto/', AddToAllView.as_view(), name="addto_all"),
    path('addto/<int:pk>/', AddToUserView.as_view(), name="addto_user"),
]
