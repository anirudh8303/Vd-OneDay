from django.db import models


class Contact(models.Model):
    person_fname = models.CharField(max_length=100)
    person_lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    subject_of_talk = models.CharField(max_length=1500)

    def __str__(self):
        return str(self.person_fname)


class UpcomingEvent(models.Model):
    event_image = models.ImageField(upload_to="vd/", default="")
    event_name = models.CharField(max_length=100)
    event_description = models.CharField(max_length=500)
    event_date = models.DateField()

    def __str__(self):
        return self.event_name


class Registerations(models.Model):
    event_name = models.ForeignKey(
        UpcomingEvent, on_delete=models.CASCADE, null=True)
    a_name = models.CharField(max_length=100)
    a_email = models.CharField(max_length=50)
    a_phone = models.IntegerField()
    a_organization = models.CharField(max_length=100)

    def __str__(self):
        return self.event_name
