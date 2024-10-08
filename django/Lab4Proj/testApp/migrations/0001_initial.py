# Generated by Django 5.0.6 on 2024-07-30 03:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('joined_date', models.DateField()),
                ('contact', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='testApp.businesscontact')),
            ],
        ),
    ]
