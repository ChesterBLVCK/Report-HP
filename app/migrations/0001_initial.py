# Generated by Django 3.2.14 on 2022-07-13 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('max', models.DecimalField(decimal_places=1, max_digits=4)),
                ('mean', models.DecimalField(decimal_places=1, max_digits=4)),
                ('min', models.DecimalField(decimal_places=1, max_digits=4)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.weatherstation')),
            ],
        ),
        migrations.CreateModel(
            name='ClinicalPharmacist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.CharField(default=False, max_length=512)),
                ('date', models.DateField()),
                ('roomNum', models.PositiveIntegerField(blank=True, null=True)),
                ('GFR', models.IntegerField(blank=True, null=True)),
                ('renal_impairment', models.BooleanField(blank=True, null=True)),
                ('Liver_Imparrenenty', models.BooleanField(blank=True, null=True)),
                ('Child_pugh_score', models.IntegerField(blank=True, null=True)),
                ('Dose_adjustment', models.BooleanField(blank=True, null=True)),
                ('Balance', models.CharField(choices=[('-V', '+Ve'), ('+V', '-Ve')], default=False, max_length=512)),
                ('intervention', models.BooleanField(blank=True, null=True)),
                ('Dose_adjustment_LI', models.BooleanField(blank=True, null=True)),
                ('Urine_output', models.CharField(choices=[('N', 'Normal'), ('O', 'Oliguria'), ('P', 'Polyuria')], default=False, max_length=512)),
                ('Feeding', models.CharField(choices=[('NPO', 'NPO'), ('Oral', 'Oral'), ('NGT/OGT', 'NGT/OGT'), ('PEG', 'PEG'), ('TPN', 'TPN')], default=False, max_length=512)),
                ('Bowel_motion', models.CharField(default=False, max_length=512)),
                ('Electrolytes_imbalance', models.CharField(choices=[('Na', 'Na'), ('K', 'K'), ('Mg', 'Mg'), ('Po4', 'Po4'), ('Ca', 'Ca')], default=False, max_length=512)),
                ('Hyper_Hypo', models.CharField(choices=[('hyper', 'hyper'), ('hypo', 'hypo')], default=False, max_length=512)),
                ('ABI', models.CharField(choices=[('Yes', 'Yes'), ('Normal', 'Normal')], default=False, max_length=512)),
                ('Metabolic_num', models.IntegerField(blank=True, null=True)),
                ('Respiratory_num', models.IntegerField(blank=True, null=True)),
                ('Metabolic', models.CharField(choices=[('Acidosis', 'Acidosis'), ('Alkalosis', 'Alkalosis')], default=False, max_length=512)),
                ('Respiratory', models.CharField(choices=[('Acidosis', 'Acidosis'), ('Alkalosis', 'Alkalosis')], default=False, max_length=512)),
                ('QT_C', models.CharField(choices=[('>500', '>500'), ('<500', '<500')], default=False, max_length=512)),
                ('QT_C_num', models.IntegerField(blank=True, null=True)),
                ('VITALS', models.CharField(choices=[('stable', 'stable'), ('tech carbon', 'techcarbon'), ('tachypnea', 'tachypnea'), ('htn', 'HTN'), ('bradycardia', 'bradycardia'), ('bradypnea', 'bradypnea'), ('hypotension', 'hypotension'), ('Fever', 'Fever')], default=False, max_length=512)),
                ('Analgesic_management', models.BooleanField(blank=True, null=True)),
                ('Sedation', models.BooleanField(blank=True, null=True)),
                ('Thromboembolic_Prophylaxis', models.CharField(choices=[('Normal', 'Normal'), ('Mechanical', 'Mechanical'), ('Pharmacology', 'Pharmacology')], default=False, max_length=512)),
                ('Stress_Ulcer_Pophylaxis', models.CharField(choices=[('Normal', 'Normal'), ('Yes', (('Pantoprazole-40-mg-IV-OD', 'Pantoprazole-40-mg-IV-OD'),))], default=False, max_length=512)),
                ('Glycemic_control_target_BG', models.BooleanField(blank=True, null=True)),
                ('T_BG', models.CharField(choices=[('G1', (('Hypoglycomic', 'Hypoglycomic'), ('Glucagon', 'Glucagon'), ('D50%', 'D50%'), ('D5%/D10%', 'D5%/D10%'))), ('G2', (('koton', 'koton'), ('Hydration', 'Hydration'))), ('G3', (('Hyperglycemia', 'Hyperglycemia'), ('Insulin Infusion', 'Insulin Infusion'), ('DKA protocol', 'DKA protocol'), ('SQ Sliding Scale', 'SQ Sliding Scale'), ('Long acting insulin', 'Long acting insulin')))], default=False, max_length=512)),
                ('Infection', models.CharField(choices=[('UA', 'UA'), ('Markers', 'Markers'), ('Fever', 'Fever'), ('Culture', 'Culture'), ('X-Ray', 'X-Ray'), ('Swab', 'Swab')], default=False, max_length=512)),
                ('Treatment', models.CharField(choices=[('Antifungal', 'Antifungal'), ('Antiviral', 'Antiviral'), ('Antimonial', 'Antimonial'), ('AB-A', (('Ampicillin', 'Ampicillin'), ('Amoxiclav', 'Amoxiclav'), ('Amikacin', 'Amikacin'), ('Azithromycin', 'Azithromycin'), ('Anidulafungin', 'Anidulafungin'), ('Albendazole', 'Albendazole'), ('Acyclovir', 'Acyclovir'))), ('AB-C', (('Cefazoline', 'Cefazoline'), ('Ceftriaxone', 'Ceftriaxone'), ('Cefotaxime', 'Cefotaxime'), ('Cefepim', 'Cefepim'), ('Ceftarolin', 'Ceftarolin'), ('Ceftazidim', 'Ceftazidim'), ('Ceftazidim/avibactam', 'Ceftazidim/avibactam'), ('Cftobiprole', 'Cftobiprole'))), ('AB-E', (('Ertapenem', 'Ertapenem'), ('Tigecycline', 'Tigecycline'))), ('AB-F', (('Flucloxacillin ', 'Flucloxacillin'), ('Fluconazole', 'Fluconazole'))), ('AB-G', (('Gentamycin', 'Gentamycin'), ('Ganciclovir', 'Ganciclovir'))), ('AB-P', (('Penicillin G', 'Penicillin G'), ('Piperacillin/tazobactam', 'Piperacillin/tazobactam'), ('Pentamidine', 'Pentamidine'))), ('AB-V', (('Vancomycin', 'Vancomycin'), ('Voriconazole', 'Voriconazole'))), ('AB-T', (('Teicoplanin', 'Teicoplanin'), ('Tigecycline', 'Tigecycline'))), ('AB-M', (('Meropenem', 'Meropenem'), ('Metronidazole', 'Metronidazole'))), ('AB-I', (('Imipenem cilastatin', 'Imipenem cilastatin'), ('Isavuconazole', 'Isavuconazole'))), ('AB-L', (('Levofloxacin', 'Levofloxacin'), ('Linezolid', 'Linezolid'))), ('AB-V', (('Voriconazole', 'Voriconazole'), ('Ganciclovir', 'Ganciclovir'))), ('AB-R', (('Remdesivir', 'Remdesivir'),))], default=False, max_length=512)),
                ('AB_INTERVENTION', models.CharField(choices=[('Intervention', (('Escalution-need', 'Escalution'), ('De-escalution-need', 'De-escalution'), ('Renal-dose-adjustment', 'Renal-dose-adjustment'), ('hepatic-dose-adjustment', 'hepatic-dose-adjustment'), ('Renal-dose-adjustment', 'Renal-dose-adjustment'), ('Discontinue', 'Discontinue')))], default=False, max_length=512)),
                ('MP_LIST', models.CharField(choices=[('Monitoring Parameter', (('Markers', 'Markers'), ('Platelets', 'Platelets'), ('QT-c', 'QT-c'), ('Level', 'Level'), ('Interaction', 'Interaction'), ('Candida_Score', 'Candida_Score'), ('Lactate', 'Lactate')))], default=False, max_length=512)),
                ('status', models.BooleanField(default=False)),
                ('MRD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.weatherstation')),
            ],
        ),
        migrations.CreateModel(
            name='AddNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.CharField(default=False, max_length=512)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('message', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField()),
                ('MRD', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.weatherstation')),
            ],
            options={
                'verbose_name': 'AddNote',
                'verbose_name_plural': 'Add Notes',
            },
        ),
    ]