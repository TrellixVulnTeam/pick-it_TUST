# Generated by Django 2.2 on 2019-05-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateField(default='1998-08-13'),
        ),
        migrations.AddField(
            model_name='profile',
            name='license_driver',
            field=models.CharField(default='', max_length=13),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='renter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='tenant',
            field=models.BooleanField(default=False),
        ),
    ]
