# Generated by Django 5.0.4 on 2024-04-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=70)),
            ],
        ),
    ]
