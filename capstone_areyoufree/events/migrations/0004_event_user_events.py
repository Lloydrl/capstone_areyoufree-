# Generated by Django 4.0.6 on 2022-08-03 18:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_alter_event_end_time_alter_event_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='user_events',
            field=models.ManyToManyField(related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
