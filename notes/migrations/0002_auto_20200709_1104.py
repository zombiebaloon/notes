# Generated by Django 3.0.7 on 2020-07-09 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='user',
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
        migrations.DeleteModel(
            name='signup',
        ),
    ]