# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-04 14:41
from __future__ import unicode_literals

import cvd_portal.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(blank=True, default='', max_length=20)),
                ('device_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default Doctor', max_length=60)),
                ('hospital', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(blank=True)),
                ('speciality', models.CharField(blank=True, max_length=100)),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('verified', models.BooleanField(default=False)),
                ('device', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='cvd_portal.Device')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('byte', models.TextField()),
                ('extra_comments_image', models.TextField(default='')),
                ('time_stamp', cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('context_of_notification', models.CharField(default='None', max_length=50)),
                ('type', models.PositiveIntegerField(null=True)),
                ('time_stamp', cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now)),
                ('priority', models.PositiveIntegerField(null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvd_portal.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField()),
                ('user_type', models.TextField()),
                ('user_type_id', models.IntegerField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Sahil', max_length=60)),
                ('date_of_birth', models.IntegerField(default=0)),
                ('gender', models.IntegerField(default=1)),
                ('UHID', models.CharField(max_length=60, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.TextField(null=True)),
                ('mobile', models.IntegerField(blank=True)),
                ('lmp', cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now)),
                ('history_high_blood_pressure', models.BooleanField(default=False)),
                ('history_of_preeclampsia', models.BooleanField(default=False)),
                ('mother_or_sister_had_preeclampsia', models.BooleanField(default=False)),
                ('history_of_obesity', models.BooleanField(default=False)),
                ('more_than_one_baby', models.BooleanField(default=False)),
                ('history_of_diseases', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systolic', models.IntegerField()),
                ('diastolic', models.IntegerField(default=0)),
                ('weight', models.IntegerField()),
                ('heart_rate', models.IntegerField()),
                ('urine_albumin', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('headache', models.BooleanField(default=False)),
                ('abdominal_pain', models.BooleanField(default=False)),
                ('visual_problems', models.BooleanField(default=False)),
                ('bleeding_per_vaginum', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('decreased_fetal_movements', models.BooleanField(default=False)),
                ('swelling_in_hands_or_face', models.BooleanField(default=False)),
                ('hyper_tension', models.BooleanField(default=False)),
                ('extra_comments', models.TextField(blank=True, default='')),
                ('time_stamp', cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='PatientDataByDoctor',
            fields=[
                ('preeclampsia', models.BooleanField(default=False)),
                ('patient_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cvd_portal.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='patientdata',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='cvd_portal.Patient'),
        ),
        migrations.AddField(
            model_name='patient',
            name='device',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='cvd_portal.Device'),
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='cvd_portal.Doctor'),
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notifications',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvd_portal.Patient'),
        ),
        migrations.AddField(
            model_name='image',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='cvd_portal.Patient'),
        ),
    ]
