# Generated by Django 2.1.4 on 2018-12-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dps_main', '0015_auto_20181210_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cause',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
    ]
