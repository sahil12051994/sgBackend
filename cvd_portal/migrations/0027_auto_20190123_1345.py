# Generated by Django 2.1.3 on 2019-01-23 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0026_auto_20190123_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='byte',
            field=models.ImageField(upload_to=''),
        ),
    ]
