# Generated by Django 3.2.13 on 2023-04-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0005_alter_annweight_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotationobject',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='annweight',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='apiannclasses',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='apianngroups',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='apiannlables',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
