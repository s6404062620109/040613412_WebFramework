# Generated by Django 5.0.6 on 2024-09-17 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('Citizenid', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=255)),
                ('Lastname', models.CharField(max_length=255)),
                ('Expire_date', models.DateField()),
                ('Blood_type', models.CharField(choices=[('o', 'O'), ('a', 'A'), ('b', 'B'), ('ab', 'AB')], default='o', max_length=5)),
            ],
        ),
    ]
