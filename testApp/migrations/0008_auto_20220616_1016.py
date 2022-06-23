# Generated by Django 3.2 on 2022-06-16 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('testApp', '0007_auto_20220615_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section_1',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='testapp_section_1', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('buttom_text', models.CharField(blank=True, max_length=50)),
                ('buttom_link', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('base_64', models.CharField(blank=True, default='', max_length=500000)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='my_placeholder',
        ),
        migrations.DeleteModel(
            name='Hello',
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]