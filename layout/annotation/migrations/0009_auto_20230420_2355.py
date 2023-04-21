# Generated by Django 3.2.13 on 2023-04-20 20:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('annotation', '0008_alter_annotationobject_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationobject',
            name='annotation_id',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='annotationobject',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterUniqueTogether(
            name='annotationobject',
            unique_together={('user', 'annotation_id')},
        ),
    ]