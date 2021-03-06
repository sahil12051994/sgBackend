# Generated by Django 2.1.5 on 2020-03-18 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swasthGarbhApp', '0013_auto_20200318_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='medicine_Image',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_extra_comments',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_freq',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_Date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_POG',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_advice_LeftUterineArteryPl',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_advice_PIGF',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_advice_RightUterineArteryPl',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_examination_anthropometry_Bmi',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_examination_anthropometry_Height',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_examination_anthropometry_Weight',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_examination_vitals_Bp',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_examination_vitals_ChestCVS',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_examination_vitals_PA',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_examination_vitals_Pr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_examination_vitals_Proteinuria',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_examination_vitals_Rr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_examination_vitals_Temp',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_general_BgNegICT',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_general_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_general_deranged_AfterBreakfast',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_general_deranged_AfterDinner',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_general_deranged_AfterLunch',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_general_deranged_Fasting',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_history_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_BloodGroup',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_GTT_1Hour',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_GTT_2Hour',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_GTT_fast',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_Hemogram',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_HusbandBloodGroup',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_Tsh',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_UrineCS',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_UrineRM',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_bloodSugar_Fasting',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_bloodSugar_PostPrandial',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_dualScreen_Bhcg',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_dualScreen_PAPP',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_level2Usg_DoneNotDone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_level2Usg_NormalAbnormal',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_ntnb_CRL',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_ntnb_Centile',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_ntnb_DoneNotDone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_ntnb_NT',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc1_investigations_ntnb_Text',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc2_Date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc2_POG',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc2_advice_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc2_examination_BP',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc2_examination_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc2_examination_PA2Weeks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc2_examination_PR',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc2_examination_Weight',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc2_history_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc2_investigations_QuadrupleScreen',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc3_Date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc3_POG',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc3_examination_BP',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc3_examination_FetalEcho',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc3_examination_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc3_examination_PA2Weeks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc3_examination_PR',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc3_examination_Weight',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc3_investigations_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_Date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_POG',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_advice_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_BP',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_CBC_HB',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_CBC_Platelets',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_CBC_TLC',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_ICT',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_KFT_Creatinine',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_KFT_UREA',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_LFT_ALP',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_LFT_OT',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_LFT_PT',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_PA2Weeks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_PR',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_UrineCulture',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_examination_Weight',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc4_history_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_Date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_POG',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_AC_centile',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_AC_cm',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_AC_weeks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_BPD_centile',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_BPD_cm',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_BPD_weeks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_CPR',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_EFW_centile',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_EFW_gm',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_EFW_weeks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_FL_centile',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_FL_cm',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_FL_weeks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_HC_centile',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_HC_cm',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_HC_weeks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_MCAPI',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_MCAPI_centile',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_UAPI',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_UAPI_centile',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_liquor_AFI',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_USG_liquor_SLP',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_advice_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_examination_BP',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_examination_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_examination_PA2Weeks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_examination_PR',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_examination_Weight',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_history_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_history_counseling_Timing',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_investigation_CBC',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_investigation_KFT',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_investigation_LFT',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc5_investigation_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_Date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_POG',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_Pelvic',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_advice_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_examination_BP',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_examination_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_examination_PA2Weeks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_examination_PR',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_examination_Weight',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc6_history_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_Date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_POG',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_advice_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_examination_BP',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_examination_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_examination_PR',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_examination_Pa2Weeks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_examination_Weight',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc7_history_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc8_Date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc8_POG',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc8_advice_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc8_examination_BP',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc8_examination_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc8_examination_PR',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc8_examination_Weight',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='anc8_history_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='investigationAncComplication',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='investigationBabyOutcome',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='investigationFtPtAbortion',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='investigationMod',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='investigations_DrugHistory',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='investigations_Others',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='obsForA',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='obsForG',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='obsForL',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pregnancydata',
            name='obsForP',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
