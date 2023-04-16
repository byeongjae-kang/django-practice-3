from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Meetup, Participant
from .forms import RegistrationForm


# Create your views here.
class MeetupsView(View):
    def get(self, request):
        meetups = Meetup.objects.all()
        return render(request, "meetups/meetups.html", {"meetups": meetups})


class MeetupDetailView(View):
    def get(self, request, slug):
        selected_meetup = Meetup.objects.get(slug=slug)
        registration_form = RegistrationForm()
        return render(
            request,
            "meetups/meetup_detail.html",
            {"meetup": selected_meetup, "form": registration_form},
        )

    def post(self, request, slug):
        registration_form = RegistrationForm(request.POST)
        selected_meetup = Meetup.objects.get(slug=slug)
        if registration_form.is_valid():
            user_email = registration_form.cleaned_data["email"]
            participant, _ = Participant.objects.get_or_create(email=user_email)
            selected_meetup.participant.add(participant)
            return redirect(reverse("success"))

        return render(
            request,
            "meetups/meetup_detail.html",
            {"meetup": selected_meetup, "form": registration_form},
        )


class ConfirmRegistrationView(View):
    def get(self, request):
        return render(request, "meetups/registration_success.html")
