from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.
class MeetupsView(View):
    def get(self, request):
        return render(request, "meetups/meetups.html")
