# Generated by Django 4.0.4 on 2022-05-26 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notogri',
            name='soz',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='notogri',
            name='togri',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='letters.togri'),
        ),
        migrations.AlterField(
            model_name='togri',
            name='soz',
            field=models.CharField(max_length=30),
        ),
    ]
