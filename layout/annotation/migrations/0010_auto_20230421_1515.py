# Generated by Django 3.2.13 on 2023-04-21 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('annotation', '0009_auto_20230420_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotationobject',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='apiannclasses',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Child_lables', to='annotation.apiannlables'),
        ),
    ]
