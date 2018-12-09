# Generated by Django 2.1.4 on 2018-12-07 14:35

from django.db import migrations, models
import dps_main.models


class Migration(migrations.Migration):

    dependencies = [
        ('dps_main', '0011_auto_20181207_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cause',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cause',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='promise',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='promise',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='promise',
            name='target_date',
            field=models.DateField(default=dps_main.models.tomorrow, help_text='The date for which the promise is expected to be redeemed'),
        ),
    ]