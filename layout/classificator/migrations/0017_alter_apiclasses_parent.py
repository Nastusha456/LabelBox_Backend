# Generated by Django 3.2.13 on 2023-05-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classificator', '0016_alter_apiclasses_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiclasses',
            name='parent',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
