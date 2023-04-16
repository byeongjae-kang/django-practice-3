from django.shortcuts import render
from django.views import View
from .models import Meetup


# Create your views here.
class MeetupsView(View):
    def get(self, request):
        meetups = Meetup.objects.all()
        return render(request, "meetups/meetups.html", {"meetups": meetups})


class MeetupDetailView(View):
    def get(self, request, slug):
        selected_meetup = Meetup.objects.get(slug=slug)
        return render(
            request, "meetups/meetup_detail.html", {"meetup": selected_meetup}
        )
