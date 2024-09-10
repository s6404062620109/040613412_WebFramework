# Generated by Django 5.0.6 on 2024-09-10 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('published_date', models.DateField(null=True)),
                ('short_detail', models.CharField(max_length=300)),
                ('demo', models.BooleanField(default=False)),
            ],
        ),
    ]
