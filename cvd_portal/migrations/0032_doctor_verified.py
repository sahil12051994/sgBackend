# Generated by Django 2.1.5 on 2019-02-02 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0031_auto_20190202_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
