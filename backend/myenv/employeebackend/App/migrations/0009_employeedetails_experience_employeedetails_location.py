# Generated by Django 5.0.4 on 2024-04-22 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_employeedetails_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetails',
            name='experience',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='location',
            field=models.CharField(default='', max_length=50),
        ),
    ]
