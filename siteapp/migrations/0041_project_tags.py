# Generated by Django 3.1.7 on 2021-02-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0040_auto_20210228_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(related_name='project', to='siteapp.Tag'),
        ),
    ]