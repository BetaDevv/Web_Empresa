# Generated by Django 2.0.2 on 2024-04-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['name'], 'verbose_name': 'enlace', 'verbose_name_plural': 'enlaces'},
        ),
        migrations.AlterField(
            model_name='link',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
