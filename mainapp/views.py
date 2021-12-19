from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm
# Create your views here.

def search_venues(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        venues = Venue.objects.filter(name__contains=searched)

        return render(request, 'search_venues.html',
                     {'searched': searched,
                      'venues': venues
                      })
    else:
        return render(request, 'search_venues.html',
                     {})

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'show_venue.html',
                  {'venue': venue})



def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'venue.html',
                  {'venue_list': venue_list})


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue? submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'venue_add.html',
                  {"form": form, 'submitted': submitted})

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'event_list.html',
                  {'event_list': event_list})

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Аня"
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    # create calendar
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M %p')


    return render(request, 'home.html', {
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    })