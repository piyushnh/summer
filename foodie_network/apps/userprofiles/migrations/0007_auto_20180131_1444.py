# Generated by Django 2.0.1 on 2018-01-31 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0006_auto_20180131_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normaluser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]