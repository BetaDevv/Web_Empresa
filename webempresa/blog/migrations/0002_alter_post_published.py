# Generated by Django 5.0.2 on 2024-03-15 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 17, 31, 56, 704158, tzinfo=datetime.timezone.utc), verbose_name='Fecha de publicacion'),
        ),
    ]
