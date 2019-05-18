# Generated by Django 2.2.1 on 2019-05-15 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20190515_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.Board'),
        ),
        migrations.AddField(
            model_name='document',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.Board'),
        ),
    ]