# Generated by Django 3.0.5 on 2020-12-19 05:13

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('channel', models.CharField(max_length=500, null=True)),
                ('game', models.CharField(max_length=100, null=True)),
                ('game_image', models.ImageField(upload_to='images')),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=200, null=True)),
                ('code', models.CharField(default=main.models.generate_code, max_length=8, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('channel', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]