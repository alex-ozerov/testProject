# Generated by Django 3.2 on 2022-06-16 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('testApp', '0008_auto_20220616_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section_2',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='testapp_section_2', serialize=False, to='cms.cmsplugin')),
                ('buttom_text_1', models.CharField(blank=True, max_length=50)),
                ('buttom_link_1', models.URLField(blank=True)),
                ('buttom_text_2', models.CharField(blank=True, max_length=50)),
                ('buttom_link_2', models.URLField(blank=True)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
