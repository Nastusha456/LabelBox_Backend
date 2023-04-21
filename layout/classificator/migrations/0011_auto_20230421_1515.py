# Generated by Django 3.2.13 on 2023-04-21 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classificator', '0010_auto_20230417_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='userobjects',
            name='classifier_id',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='apiclasses',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Child_lables', to='classificator.apilables'),
        ),
        migrations.AlterField(
            model_name='userobjects',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userobjects',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='userobjects',
            unique_together={('user', 'classifier_id')},
        ),
    ]