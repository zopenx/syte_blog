# Generated by Django 3.2.4 on 2021-06-24 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 24, 10, 14, 12, 337616, tzinfo=utc)),
        ),
    ]
