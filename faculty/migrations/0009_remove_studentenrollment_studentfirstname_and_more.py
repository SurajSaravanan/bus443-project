# Generated by Django 4.2 on 2023-04-27 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("faculty", "0008_studentenrollment_studentlastname"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentenrollment",
            name="studentfirstname",
        ),
        migrations.RemoveField(
            model_name="studentenrollment",
            name="studentlastname",
        ),
    ]
