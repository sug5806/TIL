# Generated by Django 2.2 on 2019-05-07 09:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0003_photo_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite_post', to=settings.AUTH_USER_MODEL),
        ),
    ]