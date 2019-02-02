# Generated by Django 2.1.5 on 2019-02-02 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0030_auto_20190125_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDataByDoctor',
            fields=[
                ('preeclampsia', models.BooleanField(default=False)),
                ('patient_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cvd_portal.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='cvd_portal.Doctor'),
        ),
    ]
