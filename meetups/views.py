from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
from .models import Meetup
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
        print(registration_form)
        if registration_form.is_valid():
            participant = registration_form.save()
            selected_meetup.participant.add(participant)

        return HttpResponseRedirect(reverse("meetup_detail", args=[slug]))
