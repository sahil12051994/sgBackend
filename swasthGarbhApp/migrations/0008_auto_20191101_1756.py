# Generated by Django 2.1.5 on 2019-11-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swasthGarbhApp', '0007_auto_20191101_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_Date',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_POG',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc2_Date',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc2_POG',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc3_Date',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc3_POG',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_Date',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_POG',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_Date',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_POG',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_AC_centile',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_AC_cm',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_AC_weeks',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_BPD_centile',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_BPD_cm',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_BPD_weeks',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_CPR',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_EFW_centile',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_EFW_gm',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_EFW_weeks',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_FL_centile',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_FL_cm',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_FL_weeks',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_HC_centile',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_HC_cm',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_HC_weeks',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_MCAPI',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_MCAPI_centile',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_UAPI',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_UAPI_centile',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_liquor_AFI',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_liquor_SLP',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_Date',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_POG',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_Pelvic',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_examination_BP',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_examination_PA2Weeks',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_examination_PR',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_examination_Weight',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_Date',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_POG',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_examination_BP',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_examination_PR',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_examination_Pa2Weeks',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_examination_Weight',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc8_Date',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc8_POG',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc8_examination_BP',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc8_examination_PR',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc8_examination_Weight',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='investigations_DrugHistory',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
