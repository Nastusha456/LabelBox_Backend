# Generated by Django 3.2.13 on 2023-04-06 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Weight',
            new_name='AnnWeight',
        ),
        migrations.RenameModel(
            old_name='APIClasses',
            new_name='APIAnnClasses',
        ),
        migrations.RenameModel(
            old_name='APIGroups',
            new_name='APIAnnGroups',
        ),
        migrations.RenameModel(
            old_name='APILables',
            new_name='APIAnnLables',
        ),
    ]