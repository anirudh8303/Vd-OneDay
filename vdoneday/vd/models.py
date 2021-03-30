from django.db import models


class Contact(models.Model):
    person_fname = models.CharField(max_length=100)
    person_lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    subject_of_talk = models.CharField(max_length=1500)

    def __str__(self):
        return self.phone


class UpcomingEvent(models.Model):
    event_image = models.ImageField(upload_to="vd/", default="")
    event_name = models.CharField(max_length=100)
    event_description = models.CharField(max_length=500)
    event_date = models.DateField()

    def __str__(self):
        return self.event_name
