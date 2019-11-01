# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime
from dateutil import tz
from cvd_portal.models import *

class PregnancyData(models.Model):

    patient_id = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    startDate = CustomDateTimeField(default=datetime.datetime.now)
    anc_1 = models.BooleanField(default=0)
    anc1_diabtese = models.BooleanField(default=0)
    anc1_anemia = models.BooleanField(default=0)
    anc1_hiv = models.BooleanField(default=0)
    anc1_ultrasound = models.BooleanField(default=0)
    anc1_tetnus = models.BooleanField(default=0)
    anc1_urine = models.BooleanField(default=0)
    anc1_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc1_safeDate = CustomDateTimeField(default=datetime.datetime.now)
    anc_2 = models.BooleanField(default=0)
    anc2_diabtese = models.BooleanField(default=0)
    anc2_anemia = models.BooleanField(default=0)
    anc2_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc2_safeDate = CustomDateTimeField(default=datetime.datetime.now)
    anc_3 = models.BooleanField(default=0)
    anc3_diabtese = models.BooleanField(default=0)
    anc3_anemia = models.BooleanField(default=0)
    anc3_urine = models.BooleanField(default=0)
    anc3_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc3_safeDate = CustomDateTimeField(default=datetime.datetime.now)
    anc_4 = models.BooleanField(default=0)
    anc4_diabtese = models.BooleanField(default=0)
    anc4_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc4_safeDate = CustomDateTimeField(default=datetime.datetime.now)
    anc_5 = models.BooleanField(default=0)
    anc5_diabtese = models.BooleanField(default=0)
    anc5_urine = models.BooleanField(default=0)
    anc5_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc5_safeDate = CustomDateTimeField(default=datetime.datetime.now)
    anc_6 = models.BooleanField(default=0)
    anc6_diabtese = models.BooleanField(default=0)
    anc6_anemia = models.BooleanField(default=0)
    anc6_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc6_safeDate = CustomDateTimeField(default=datetime.datetime.now)
    anc_7 = models.BooleanField(default=0)
    anc7_diabtese = models.BooleanField(default=0)
    anc7_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc7_safeDate = CustomDateTimeField(default=datetime.datetime.now)
    anc_8 = models.BooleanField(default=0)
    anc8_diabtese = models.BooleanField(default=0)
    anc8_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc8_safeDate = CustomDateTimeField(default=datetime.datetime.now)
    anc8_his_breath = models.BooleanField(default=0)
    anc8_his_fatigue = models.BooleanField(default=0)
    anc8_his_head = models.BooleanField(default=0)
    anc8_his_bleed = models.BooleanField(default=0)
    anc8_his_burn = models.BooleanField(default=0)
    anc8_his_fetal_move = models.BooleanField(default=0)
    anc8_his_itching = models.BooleanField(default=0)
    anc8_exam_pallor = models.BooleanField(default=0)
    anc8_exam_pedal = models.BooleanField(default=0)
    anc8_exam_pa = models.BooleanField(default=0)
    anc8_advice_DFMC = models.BooleanField(default=0)
    anc8_advice_Fe_Ca = models.BooleanField(default=0)
    anc8_advice_induction = models.BooleanField(default=0)
    time_stamp = CustomDateTimeField(default=datetime.datetime.now)
    invest_chronic_hyper = models.BooleanField(default=0)
    invest_type_2_diabetes = models.BooleanField(default=0)
    invest_RHD_native = models.BooleanField(default=0)
    invest_RHD_post = models.BooleanField(default=0)
    invest_acyanotic = models.BooleanField(default=0)
    invest_cyanotic = models.BooleanField(default=0)
    invest_chronic_liver = models.BooleanField(default=0)
    invest_chronic_kidney = models.BooleanField(default=0)
    invest_APLA = models.BooleanField(default=0)
    invest_SLE = models.BooleanField(default=0)
    anc1_his_fever = models.BooleanField(default=0)
    anc1_his_rash = models.BooleanField(default=0)
    anc1_his_nausea_vomit = models.BooleanField(default=0)
    anc1_his_bleed = models.BooleanField(default=0)
    anc1_his_abdpain = models.BooleanField(default=0)
    anc1_drugin = models.BooleanField(default=0)
    anc1_his_smoke = models.BooleanField(default=0)
    anc1_his_alcohol = models.BooleanField(default=0)
    anc1_his_tob = models.BooleanField(default=0)
    anc1_his_caff = models.BooleanField(default=0)
    anc1_his_int = models.BooleanField(default=0)
    anc1_exam_pallor = models.BooleanField(default=0)
    anc1_exam_lcterus = models.BooleanField(default=0)
    anc1_exam_clubbing = models.BooleanField(default=0)
    anc1_exam_cyanosis = models.BooleanField(default=0)
    anc1_exam_edem = models.BooleanField(default=0)
    anc1_exam_lymp = models.BooleanField(default=0)
    anc1_invest_HIV = models.BooleanField(default=0)
    anc1_invest_hbsag = models.BooleanField(default=0)
    anc1_invest_VDRL = models.BooleanField(default=0)
    anc1_invest_urineRM = models.BooleanField(default=0)
    anc1_invest_urineCS = models.BooleanField(default=0)
    anc1_invest_CRL = models.BooleanField(default=0)
    anc1_invest_NT = models.BooleanField(default=0)
    anc1_invest_centile = models.BooleanField(default=0)
    anc1_invest_text = models.BooleanField(default=0)
    anc1_advice_Tfolate = models.BooleanField(default=0)
    anc1_advice_TFe = models.BooleanField(default=0)
    anc1_general_TSH = models.BooleanField(default=0)
    anc1_general_T_nitro = models.BooleanField(default=0)
    anc1_general_syp = models.BooleanField(default=0)
    anc1_general_Tvit = models.BooleanField(default=0)
    anc1_general_plenty = models.BooleanField(default=0)
    anc2_his_breath = models.BooleanField(default=0)
    anc2_his_fatigue = models.BooleanField(default=0)
    anc2_his_head = models.BooleanField(default=0)
    anc2_his_bleed = models.BooleanField(default=0)
    anc2_his_burn = models.BooleanField(default=0)
    anc2_his_quick_percieve = models.BooleanField(default=0)
    anc2_exam_pallor = models.BooleanField(default=0)
    anc2_exam_pedal = models.BooleanField(default=0)
    anc2_exam_pa = models.BooleanField(default=0)
    anc2_invest_quad = models.BooleanField(default=0)
    anc2_invest_fetal = models.BooleanField(default=0)
    anc2_advice_OGTT = models.BooleanField(default=0)
    anc2_advice_TFe = models.BooleanField(default=0)
    anc2_advice_TCa = models.BooleanField(default=0)
    anc2_advice_Hb_Talb = models.BooleanField(default=0)
    anc2_advice_Hb_TFe = models.BooleanField(default=0)
    anc2_advice_Hb_HPLC = models.BooleanField(default=0)
    anc2_advice_Hb_peri = models.BooleanField(default=0)
    anc2_advice_Hb_serum = models.BooleanField(default=0)
    anc2_advice_tetanus = models.BooleanField(default=0)
    anc3_his_breath = models.BooleanField(default=0)
    anc3_his_fatigue = models.BooleanField(default=0)
    anc3_his_head = models.BooleanField(default=0)
    anc3_his_bleed = models.BooleanField(default=0)
    anc3_his_leak = models.BooleanField(default=0)
    anc3_his_burn = models.BooleanField(default=0)
    anc3_his_fetal_move = models.BooleanField(default=0)
    anc3_his_itching = models.BooleanField(default=0)
    anc3_exam_pallor = models.BooleanField(default=0)
    anc3_exam_pedal = models.BooleanField(default=0)
    anc3_exam_pa = models.BooleanField(default=0)
    anc3_invest_GTT_fast = models.BooleanField(default=0)
    anc3_invest_GTT_1hr  = models.BooleanField(default=0)
    anc3_invest_GTT_2hr  = models.BooleanField(default=0)
    anc3_invest_CBC = models.BooleanField(default=0)
    anc3_invest_urine = models.BooleanField(default=0)
    anc3_invest_ICT = models.BooleanField(default=0)
    anc3_advice_TFe = models.BooleanField(default=0)
    anc3_advice_DFMC = models.BooleanField(default=0)
    anc3_advice_BleedPV = models.BooleanField(default=0)
    anc3_advice_spotPV = models.BooleanField(default=0)
    anc3_advice_leakPV = models.BooleanField(default=0)
    anc3_advice_fetalmove = models.BooleanField(default=0)
    anc3_advice_abdpain = models.BooleanField(default=0)
    anc3_advice_injAntiD = models.BooleanField(default=0)
    anc4_his_breath = models.BooleanField(default=0)
    anc4_his_fatigue = models.BooleanField(default=0)
    anc4_his_head = models.BooleanField(default=0)
    anc4_his_bleed = models.BooleanField(default=0)
    anc4_his_burn = models.BooleanField(default=0)
    anc4_his_fetal_move = models.BooleanField(default=0)
    anc4_his_itching = models.BooleanField(default=0)
    anc4_exam_pallor = models.BooleanField(default=0)
    anc4_exam_pedal = models.BooleanField(default=0)
    anc4_exam_pa = models.BooleanField(default=0)
    anc4_advice_TFe = models.BooleanField(default=0)
    anc4_advice_TCa = models.BooleanField(default=0)
    anc4_advice_DFMC = models.BooleanField(default=0)
    anc4_advice_BleedPV = models.BooleanField(default=0)
    anc4_advice_spotPV = models.BooleanField(default=0)
    anc4_advice_leakPV = models.BooleanField(default=0)
    anc4_advice_fetalmove = models.BooleanField(default=0)
    anc4_advice_abdpain = models.BooleanField(default=0)
    anc4_advice_injAntiD = models.BooleanField(default=0)
    anc4_advice_USG = models.BooleanField(default=0)
    anc5_his_breath = models.BooleanField(default=0)
    anc5_his_fatigue = models.BooleanField(default=0)
    anc5_his_head = models.BooleanField(default=0)
    anc5_his_bleed = models.BooleanField(default=0)
    anc5_his_burn = models.BooleanField(default=0)
    anc5_his_fetal_move = models.BooleanField(default=0)
    anc5_his_itching = models.BooleanField(default=0)
    anc5_his_vaginal_del = models.BooleanField(default=0)
    anc5_his_LSCS_del = models.BooleanField(default=0)
    anc5_his_birth_attendant = models.BooleanField(default=0)
    anc5_exam_pallor = models.BooleanField(default=0)
    anc5_exam_pedal = models.BooleanField(default=0)
    anc5_exam_pa = models.BooleanField(default=0)
    anc5_invest_CBC = models.BooleanField(default=0)
    anc5_invest_LFT = models.BooleanField(default=0)
    anc5_invest_KFT = models.BooleanField(default=0)
    anc5_invest_CPR = models.CharField(max_length= 100, default="", blank=True)
    anc5_advice_DFMC = models.BooleanField(default=0)
    anc5_advice_TFe_Ca = models.BooleanField(default=0)
    anc5_advice_BleedPV = models.BooleanField(default=0)
    anc5_advice_spotPV = models.BooleanField(default=0)
    anc5_advice_leakPV = models.BooleanField(default=0)
    anc5_advice_fetalmove = models.BooleanField(default=0)
    anc5_advice_abdpain = models.BooleanField(default=0)
    anc5_advice_NST = models.BooleanField(default=0)
    anc6_his_breath = models.BooleanField(default=0)
    anc6_his_fatigue = models.BooleanField(default=0)
    anc6_his_head = models.BooleanField(default=0)
    anc6_his_bleed = models.BooleanField(default=0)
    anc6_his_burn = models.BooleanField(default=0)
    anc6_his_fetal_move = models.BooleanField(default=0)
    anc6_his_itching = models.BooleanField(default=0)
    anc6_exam_pallor = models.BooleanField(default=0)
    anc6_exam_pedal = models.BooleanField(default=0)
    anc6_exam_pa = models.BooleanField(default=0)
    anc6_advice_DFMC = models.BooleanField(default=0)
    anc6_advice_TFe_Ca = models.BooleanField(default=0)
    anc6_advice_BleedPV = models.BooleanField(default=0)
    anc6_advice_spotPV = models.BooleanField(default=0)
    anc6_advice_leakPV = models.BooleanField(default=0)
    anc6_advice_fetalmove = models.BooleanField(default=0)
    anc6_advice_abdpain = models.BooleanField(default=0)
    anc6_advice_NST = models.BooleanField(default=0)
    anc7_his_breath = models.BooleanField(default=0)
    anc7_his_fatigue = models.BooleanField(default=0)
    anc7_his_head = models.BooleanField(default=0)
    anc7_his_bleed = models.BooleanField(default=0)
    anc7_his_burn = models.BooleanField(default=0)
    anc7_his_fetal_move = models.BooleanField(default=0)
    anc7_his_itching = models.BooleanField(default=0)
    anc7_exam_pallor = models.BooleanField(default=0)
    anc7_exam_pedal = models.BooleanField(default=0)
    anc7_exam_pa = models.BooleanField(default=0)
    anc7_advice_DFMC = models.BooleanField(default=0)
    anc7_advice_TFe_Ca = models.BooleanField(default=0)
    anc7_advice_BleedPV = models.BooleanField(default=0)
    anc7_advice_spotPV = models.BooleanField(default=0)
    anc7_advice_leakPV = models.BooleanField(default=0)
    anc7_advice_fetalmove = models.BooleanField(default=0)
    anc7_advice_abdpain = models.BooleanField(default=0)
    invest_others = models.CharField(max_length= 100, default="",   blank=True)
    invest_drug_history = models.CharField(max_length= 100, default="",   blank=True)
    anc_1_date = models.CharField(max_length= 100,blank=True, default="")
    anc_1_POG = models.CharField(max_length= 100, default="",   blank=True)
    anc1_his_others = models.CharField(max_length= 100, default="", blank=True)
    anc1_exam_height = models.CharField(max_length= 100, default="",   blank=True)
    anc1_exam_weight = models.CharField(max_length= 100, default="",   blank=True)
    anc1_exam_BMI = models.CharField(max_length= 100, default="",   blank=True)
    anc1_exam_PR = models.CharField(max_length= 100, default="",   blank=True)
    anc1_exam_BP = models.CharField(max_length= 100, default="",   blank=True)
    anc1_exam_RR = models.CharField(max_length= 100, default="",   blank=True)
    anc1_exam_temp = models.CharField(max_length= 100, default="",   blank=True)
    anc1_exam_proteinuria = models.CharField(max_length= 100, default="",   blank=True)
    anc1_exam_chest = models.CharField(max_length= 100, default="",   blank=True)
    anc1_exam_PA = models.CharField(max_length= 100, default="",   blank=True)
    anc1_exam_others = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_bg = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_husband_bg = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_hemo = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_bloodsugar_fast = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_bloodsugar_post = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_GTT_fast  = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_GTT_1hr = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_GTT_2hr  = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_TSH = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_NT_done = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_PAPP = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_b_hcg = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_levelII_done = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_normal = models.CharField(max_length= 100, default="",   blank=True)
    anc1_invest_others = models.CharField(max_length= 100, default="",   blank=True)
    anc1_general_nutritional = models.CharField(max_length= 100, default="",   blank=True)
    anc_1_GeneralDeranged_fasting = models.CharField(max_length= 100, default="",   blank=True)
    anc_1_GeneralDeranged_breakfast = models.CharField(max_length= 100, default="",   blank=True)
    anc_1_GeneralDeranged_lunch = models.CharField(max_length= 100, default="",   blank=True)
    anc_1_GeneralDeranged_dinner = models.CharField(max_length= 100, default="",   blank=True)
    anc1_general_ailment = models.CharField(max_length= 100, default="",   blank=True)
    anc1_general_ICT = models.CharField(max_length= 100, default="",   blank=True)
    anc1_general_others = models.CharField(max_length= 100, default="",   blank=True)
    anc2_POG = models.CharField(max_length= 100, default="",   blank=True)
    anc_2_pa_2weeks= models.CharField(max_length= 100, default="",   blank=True)
    anc2_his_others = models.CharField(max_length= 100, default="",   blank=True)
    anc2_exam_PR = models.CharField(max_length= 100, default="",   blank=True)
    anc2_exam_BP = models.CharField(max_length= 100, default="",   blank=True)
    anc2_exam_weight = models.CharField(max_length= 100, default="",   blank=True)
    anc2_exam_others = models.CharField(max_length= 100, default="",   blank=True)
    anc2_invest_others = models.CharField(max_length= 100, default="",   blank=True)
    anc2_advice_nutri = models.CharField(max_length= 100, default="",   blank=True)
    anc2_advice_general = models.CharField(max_length= 100, default="",   blank=True)
    anc2_advice_common = models.CharField(max_length= 100, default="",   blank=True)
    anc2_advice_others = models.CharField(max_length= 100, default="",   blank=True)
    anc3_his_others  = models.CharField(max_length= 100, default="",   blank=True)
    anc3_exam_PR = models.CharField(max_length= 100, default="",   blank=True)
    anc3_exam_BP = models.CharField(max_length= 100, default="",   blank=True)
    anc_3_pa_2weeks= models.CharField(max_length= 100, default="",   blank=True)
    anc3_exam_weight = models.CharField(max_length= 100, default="",   blank=True)
    anc3_investigation_others= models.CharField(max_length= 100, default="",   blank=True)
    anc3_exam_others = models.CharField(max_length= 100, default="",   blank=True)
    anc3_advice_nutri = models.CharField(max_length= 100, default="",   blank=True)
    anc3_advice_general = models.CharField(max_length= 100, default="",   blank=True)
    anc3_advice_common = models.CharField(max_length= 100, default="",   blank=True)
    anc3_advice_others = models.CharField(max_length= 100, default="",   blank=True)
    anc4_his_others = models.CharField(max_length= 100, default="",   blank=True)
    anc4_exam_PR = models.CharField(max_length= 100, default="",   blank=True)
    anc4_exam_BP = models.CharField(max_length= 100, default="",   blank=True)
    anc_4_pa_2weeks = models.CharField(max_length= 100, default="",   blank=True)
    anc4_exam_weight = models.CharField(max_length= 100, default="",   blank=True)
    anc4_exam_others = models.CharField(max_length= 100, default="",   blank=True)
    anc4_advice_nutri = models.CharField(max_length= 100, default="",   blank=True)
    anc4_advice_general = models.CharField(max_length= 100, default="",   blank=True)
    anc4_advice_common = models.CharField(max_length= 100, default="",   blank=True)
    anc4_advice_others = models.CharField(max_length= 100, default="",   blank=True)
    anc5_his_others = models.CharField(max_length= 100, default="",   blank=True)
    anc5_his_timing = models.CharField(max_length= 100, default="",   blank=True)
    anc5_his_timing = models.CharField(max_length= 100, default="",   blank=True)
    anc5_exam_BP = models.CharField(max_length= 100, default="",   blank=True)
    anc_5_pa_2weeks = models.CharField(max_length= 100, default="",   blank=True)
    anc5_exam_weight = models.CharField(max_length= 100, default="",   blank=True)
    anc5_exam_others = models.CharField(max_length= 100, default="",   blank=True)
    anc5_invest_others = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_BPD_cm = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_BPD_weeks = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_BPD_centile = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_HC_cm = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_HC_weeks = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_HC_centile = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_AC_cm = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_AC_weeks = models.CharField(max_length= 100, default="",   blank=True )
    anc5_USG_AC_weeks = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_AC_centile = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_FL_cm = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_FL_weeks = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_FL_centile = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_EFW_gm  = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_EFW_weeks = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_EFW_centile = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_liquor_SLP = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_liquor_AFI = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_UAPI = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_UAPI_centile = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_MCAPI = models.CharField(max_length= 100, default="",   blank=True)
    anc5_USG_MCAPI_centile = models.CharField(max_length= 100, default="",   blank=True)
    anc5_advice_nutri = models.CharField(max_length= 100, default="",   blank=True)
    anc5_advice_general = models.CharField(max_length= 100, default="",   blank=True)
    anc5_advice_common = models.CharField(max_length= 100, default="",   blank=True)
    anc5_advice_others = models.CharField(max_length= 100, default="",   blank=True)
    anc6_his_others = models.CharField(max_length= 100, default="",   blank=True)
    anc6_exam_PR = models.CharField(max_length= 100, default="",   blank=True)
    anc6_exam_BP = models.CharField(max_length= 100, default="",   blank=True)
    anc6_pa_2weeks= models.CharField(max_length= 100, default="",   blank=True)
    anc6_exam_weight = models.CharField(max_length= 100, default="",   blank=True)
    anc6_exam_others = models.CharField(max_length= 100, default="",   blank=True)
    anc6_exam_pelvic = models.CharField(max_length= 100, default="",   blank=True)
    anc6_advice_others  = models.CharField(max_length= 100, default="",   blank=True)
    anc7_his_others = models.CharField(max_length= 100, default="",   blank=True)
    anc7_exam_PR = models.CharField(max_length= 100, default="",   blank=True)
    anc7_exam_BP = models.CharField(max_length= 100, default="",   blank=True)
    anc7_pa_2weeks = models.CharField(max_length= 100, default="",   blank=True)
    anc7_exam_weight = models.CharField(max_length= 100, default="",   blank=True)
    anc7_exam_others = models.CharField(max_length= 100, default="",   blank=True)
    anc7_advice_others = models.CharField(max_length= 100, default="",   blank=True)
    anc8_his_others = models.CharField(max_length= 100, default="",   blank=True)
    anc8_exam_PR = models.CharField(max_length= 100, default="",   blank=True)
    anc8_exam_BP = models.CharField(max_length= 100, default="",   blank=True)
    anc8_exam_weight = models.CharField(max_length= 100, default="",   blank=True)
    anc8_exam_others = models.CharField(max_length= 100, default="",   blank=True)
    anc8_advice_others = models.CharField(max_length= 100, default="",   blank=True)



class Medicine(models.Model):
    patient_id = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        null=True
    )
    medicine_name = models.CharField(max_length=50)
    medicine_freq = models.CharField(max_length=50, default="",)
    medicine_Image = models.TextField(default="",)
    medicine_extra_comments = models.TextField(default="",)
    medicine_start = CustomDateTimeField(default=datetime.datetime.now)
    medicine_end = CustomDateTimeField(default=datetime.datetime.now)
    isSOS = models.BooleanField(default=False)

class Hospital(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patientsPregHospitals')
    xCoordinate = models.DecimalField(max_digits = 20, decimal_places = 15)
    yCoordinate = models.DecimalField(max_digits = 20, decimal_places = 15)

class Complication(models.Model):
    informationByDoc = models.TextField()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patientsComplication')
    complicationImage = models.TextField()
    tookAction = models.BooleanField(default=0)
    informationByPatient = models.TextField()
