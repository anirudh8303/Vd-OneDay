# Generated by Django 3.1.3 on 2021-03-30 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_image', models.ImageField(upload_to='')),
                ('event_name', models.CharField(max_length=100)),
                ('event_description', models.CharField(max_length=500)),
                ('event_date', models.DateField()),
            ],
        ),
    ]
