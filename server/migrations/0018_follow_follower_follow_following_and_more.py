# Generated by Django 4.2.13 on 2024-12-15 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0017_remove_follow_followedid_remove_follow_userid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='follower',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('follower', 'following')},
        ),
        migrations.RemoveField(
            model_name='follow',
            name='userid',
        ),
    ]