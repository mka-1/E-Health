# Generated by Django 3.2 on 2021-04-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorReg', '0002_rename_birth_doctorinfo_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorinfo',
            name='usernameDr',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
