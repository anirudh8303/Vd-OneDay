from django.shortcuts import render
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


def contact(request):
    if request.method == "POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['sub']

        contact = Contact(person_fname=fname, person_lname=lname,
                          email=email, phone=phone, subject_of_talk=subject)
        contact.save()
        messages.success(request, "Your review is submitted")

        return render(request, 'vd/base.html')
