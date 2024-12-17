# Generated by Django 4.2.13 on 2024-12-15 13:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0016_user_lastactive_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='followedid',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='userid',
        ),
        migrations.AddField(
            model_name='follow',
            name='userid',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]