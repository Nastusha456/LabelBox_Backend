# Generated by Django 3.2.13 on 2023-04-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0007_auto_20230417_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotationobject',
            name='Weight',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
