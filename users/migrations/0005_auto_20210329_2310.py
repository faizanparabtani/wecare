# Generated by Django 3.1.2 on 2021-03-29 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210327_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='ethnicity',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='speciality',
        ),
    ]
