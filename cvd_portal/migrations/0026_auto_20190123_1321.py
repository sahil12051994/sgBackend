# Generated by Django 2.1.3 on 2019-01-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0025_auto_20181119_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='byte',
            field=models.FileField(upload_to=''),
        ),
    ]