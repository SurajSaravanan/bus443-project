# Generated by Django 4.2 on 2023-04-27 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("faculty", "0003_award_facultynomination"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Award",
        ),
        migrations.DeleteModel(
            name="Facultycomment",
        ),
        migrations.DeleteModel(
            name="FacultyInfo",
        ),
        migrations.DeleteModel(
            name="FacultyNomination",
        ),
    ]