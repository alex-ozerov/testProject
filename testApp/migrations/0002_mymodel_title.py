# Generated by Django 3.2 on 2022-06-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='title'),
            preserve_default=False,
        ),
    ]
