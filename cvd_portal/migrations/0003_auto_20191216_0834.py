# Generated by Django 2.1.5 on 2019-12-16 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0002_auto_20191111_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='spinnerEducation',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='spinnerStatus',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
