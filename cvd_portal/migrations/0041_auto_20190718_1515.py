# Generated by Django 2.1.5 on 2019-07-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0040_auto_20190718_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='extra_comments',
            field=models.TextField(default='null', null=True),
        ),
    ]
