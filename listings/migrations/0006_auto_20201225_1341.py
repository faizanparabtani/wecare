# Generated by Django 3.1.2 on 2020-12-25 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20201219_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='id',
        ),
        migrations.AddField(
            model_name='listing',
            name='listing_id',
            field=models.AutoField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
