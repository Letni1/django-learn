# Generated by Django 2.0.5 on 2018-05-20 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='view',
            field=models.PositiveIntegerField(default=0),
        ),
    ]