# Generated by Django 5.0.4 on 2024-04-07 18:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_referals'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='referals',
        ),
        migrations.AddField(
            model_name='user',
            name='referer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]