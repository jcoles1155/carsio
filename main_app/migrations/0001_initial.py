# Generated by Django 3.2 on 2021-04-28 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('make', models.CharField(max_length=50)),
                ('carModel', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('body', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
