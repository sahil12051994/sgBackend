# Generated by Django 2.1.5 on 2019-05-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0033_merge_20190207_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='UHID',
            field=models.CharField(default='abc123', max_length=60),
        ),
    ]
