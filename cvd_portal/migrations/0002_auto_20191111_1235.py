# Generated by Django 2.1.5 on 2019-11-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='spinnerEducation',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='spinnerStatus',
            field=models.CharField(max_length=60, null=True),
        ),
    ]