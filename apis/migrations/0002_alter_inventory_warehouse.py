# Generated by Django 3.2.13 on 2022-05-16 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apis.warehouse'),
        ),
    ]
