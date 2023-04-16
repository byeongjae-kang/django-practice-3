from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

MEETUP_DATA = [
    {"title": "title", "location": "location", "slug": "title"},
    {"title": "title", "location": "location", "slug": "title"},
    {"title": "title", "location": "location", "slug": "title"},
]


# Create your views here.
class MeetupsView(View):
    def get(self, request):
        return render(request, "meetups/meetups.html", {"meetups": MEETUP_DATA})


class MeetupDetailView(View):
    def get(self, request, slug):
        selected_meetup = {
            "title": "A first meetup",
            "description": "This is the first meetup",
        }
        return render(
            request, "meetups/meetup_detail.html", {"meetup": selected_meetup}
        )
