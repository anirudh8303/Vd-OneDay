from django.shortcuts import render, redirect
from .models import Contact, UpcomingEvent
from django.contrib import messages


def home(request):
    return render(request, 'vd/base.html')


def event(request):
    return render(request, 'vd/events.html')


def upevent(request):
    event_list = UpcomingEvent.objects.all()
    params = {
        'eventlist': event_list,
    }
    return render(request, 'vd/upcomingevents.html', params)


def pastevent(request):
    return render(request, 'vd/past_events.html')


def contact(request):
    if request.method == "POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['sub']

        contact = Contact(person_fname=fname, person_lname=lname,
                          email=email, subject_of_talk=subject)
        contact.save()
        messages.success(request, "Your review is submitted")

        return redirect('/')
