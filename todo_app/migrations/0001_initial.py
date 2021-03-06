# Generated by Django 3.1.2 on 2020-10-17 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
