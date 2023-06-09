# Generated by Django 3.2.13 on 2023-04-17 19:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0006_auto_20230417_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotationobject',
            name='Weight',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='apiannclasses',
            name='groups',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='apiannclasses',
            name='lables',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='apiannclasses',
            name='position_x',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='apiannclasses',
            name='position_y',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='apianngroups',
            name='position_x',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='apianngroups',
            name='position_y',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='apiannlables',
            name='position_x',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='apiannlables',
            name='position_y',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
        migrations.DeleteModel(
            name='AnnWeight',
        ),
    ]
