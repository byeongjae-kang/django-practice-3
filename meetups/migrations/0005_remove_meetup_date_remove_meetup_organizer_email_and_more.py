# Generated by Django 4.2 on 2023-04-16 10:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("meetups", "0004_participant_meetup_date_meetup_organizer_email_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="meetup",
            name="date",
        ),
        migrations.RemoveField(
            model_name="meetup",
            name="organizer_email",
        ),
        migrations.RemoveField(
            model_name="meetup",
            name="participant",
        ),
    ]