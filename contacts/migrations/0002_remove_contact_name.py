# Generated by Django 3.2.7 on 2021-09-13 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
    ]