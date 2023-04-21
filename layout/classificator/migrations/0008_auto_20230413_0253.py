# Generated by Django 3.2.13 on 2023-04-12 23:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classificator', '0007_classifier'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserObjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.ManyToManyField(to='classificator.APIClasses')),
                ('groups', models.ManyToManyField(to='classificator.APIGroups')),
                ('labels', models.ManyToManyField(to='classificator.APILables')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Classifier',
        ),
    ]
