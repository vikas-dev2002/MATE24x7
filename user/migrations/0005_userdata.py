# Generated by Django 3.2.4 on 2023-01-14 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_worker_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('amobile', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=40)),
                ('address', models.TextField()),
                ('job', models.CharField(max_length=40)),
            ],
        ),
    ]
