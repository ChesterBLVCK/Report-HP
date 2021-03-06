# Generated by Django 3.2.14 on 2022-07-13 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220713_1414'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hospitalmrd',
            options={'verbose_name': 'HospitalMRD', 'verbose_name_plural': ' Hospital MRD '},
        ),
        migrations.RemoveField(
            model_name='addnote',
            name='MRD',
        ),
        migrations.RemoveField(
            model_name='addnote',
            name='status',
        ),
        migrations.RemoveField(
            model_name='clinicalpharmacist',
            name='roomNum',
        ),
        migrations.AlterField(
            model_name='addnote',
            name='patient',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.clinicalpharmacist'),
        ),
    ]
