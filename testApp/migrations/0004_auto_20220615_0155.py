# Generated by Django 3.2 on 2022-06-14 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0003_hello'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hello',
            name='guest_name',
        ),
        migrations.AddField(
            model_name='hello',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='hello',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
