# Generated by Django 3.2 on 2022-06-15 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0004_auto_20220615_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='hello',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]