# Generated by Django 3.1.2 on 2020-12-18 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_auto_20201208_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('provider', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.provider')),
                ('ethnicity', models.CharField(max_length=20)),
                ('consultation_charges', models.IntegerField()),
            ],
        ),
    ]
