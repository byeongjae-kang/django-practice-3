from django.urls import path
from . import views

urlpatterns = [
    path("meetups/", views.MeetupsView.as_view(), name="meetups"),
    path(
        "meetups/<slug:slug>/success",
        views.ConfirmRegistrationView.as_view(),
        name="success",
    ),
    path("meetups/<slug:slug>", views.MeetupDetailView.as_view(), name="meetup_detail"),
]
