# Generated by Django 3.1.3 on 2021-03-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vd', '0002_upcomingevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevent',
            name='event_image',
            field=models.ImageField(default='', upload_to='vd/'),
        ),
    ]
