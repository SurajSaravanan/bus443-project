# Generated by Django 4.2 on 2023-04-27 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faculty", "0009_remove_studentenrollment_studentfirstname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentenrollment",
            name="enrollmentid",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
