# Generated by Django 2.2.2 on 2019-06-24 07:32

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]