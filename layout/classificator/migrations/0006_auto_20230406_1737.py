# Generated by Django 3.2.13 on 2023-04-06 14:37

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classificator', '0005_remove_apiclasses_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiclasses',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Child_lables', to='classificator.apilables'),
        ),
        migrations.RemoveField(
            model_name='apiclasses',
            name='groups',
        ),
        migrations.AddField(
            model_name='apiclasses',
            name='groups',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=list, size=None),
        ),
        migrations.RemoveField(
            model_name='apiclasses',
            name='lables',
        ),
        migrations.AddField(
            model_name='apiclasses',
            name='lables',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=list, size=None),
        ),
    ]