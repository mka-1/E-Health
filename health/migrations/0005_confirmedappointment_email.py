# Generated by Django 3.2 on 2021-04-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0004_alter_confirmedappointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmedappointment',
            name='email',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]