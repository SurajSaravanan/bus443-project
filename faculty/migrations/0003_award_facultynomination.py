# Generated by Django 4.2 on 2023-04-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faculty", "0002_facultycomment_studentinfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Award",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("awardtype", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="FacultyNomination",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("facultyname", models.CharField(max_length=100)),
                ("awardtype", models.CharField(max_length=100)),
            ],
        ),
    ]
