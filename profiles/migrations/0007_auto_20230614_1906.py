# Generated by Django 3.2.19 on 2023-06-14 19:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20230614_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(300), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(300), django.core.validators.MinValueValidator(1)]),
        ),
    ]