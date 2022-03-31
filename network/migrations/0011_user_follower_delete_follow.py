# Generated by Django 4.0.3 on 2022-03-31 05:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_remove_follow_followers_remove_follow_following_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follower',
            field=models.ManyToManyField(related_name='follows', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
