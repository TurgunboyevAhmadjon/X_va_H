# Generated by Django 4.0.4 on 2022-05-24 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notogri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soz', models.CharField(max_length=40)),
                ('togri', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Togri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soz', models.CharField(max_length=50)),
            ],
        ),
    ]