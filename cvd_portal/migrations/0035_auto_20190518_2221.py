# Generated by Django 2.1.5 on 2019-05-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0034_patient_uhid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='UHID',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
