# Generated by Django 3.2.13 on 2023-03-19 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classificator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apiclasses',
            name='cl_id',
        ),
        migrations.RemoveField(
            model_name='apigroups',
            name='gr_id',
        ),
        migrations.RemoveField(
            model_name='apilables',
            name='la_id',
        ),
    ]
