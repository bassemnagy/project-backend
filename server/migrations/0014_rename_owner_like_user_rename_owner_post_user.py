# Generated by Django 4.2.13 on 2024-12-14 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0013_rename_id_like_likeid_rename_id_post_postid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='owner',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='owner',
            new_name='user',
        ),
    ]
