# Generated by Django 2.1 on 2019-05-02 04:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0003_auto_20190501_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='insta',
            name='like',
            field=models.ManyToManyField(related_name='like_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
