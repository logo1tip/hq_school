# Generated by Django 4.2.6 on 2023-10-24 16:37

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0002_alter_lessonviewinfo_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lessonviewinfo',
            unique_together={('lesson', 'user')},
        ),
        migrations.AddField(
            model_name='lessonviewinfo',
            name='last_view_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 24, 16, 37, 35, 945310)),
        ),
    ]
