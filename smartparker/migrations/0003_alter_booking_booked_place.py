# Generated by Django 3.2.7 on 2021-09-19 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartparker', '0002_booking_rentimages_rentregister_report_reportimages_slotsplace_userprofile_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booked_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartparker.rentregister'),
        ),
    ]