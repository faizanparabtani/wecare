# Generated by Django 3.1.2 on 2021-04-24 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_isconsulting_date_removed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='isconsulting',
            name='date_removed',
            field=models.DateTimeField(blank=True),
        ),
    ]
