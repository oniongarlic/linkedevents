# Generated by Django 2.2.11 on 2020-11-18 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0077_auto_20200803_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_virtualevent',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
