# Generated by Django 2.1.4 on 2018-12-07 01:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='A full description of the cause. This will be displayed to the user')),
                ('illustration', models.ImageField(help_text='Images associated with the cause', upload_to='')),
                ('primary_contact', models.CharField(help_text='Full name of the contact associated with the cause', max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('expiration_date', models.DateTimeField()),
                ('target_amount', models.FloatField()),
                ('currency', models.CharField(max_length=10)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('enabled', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Promise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(help_text='Amount promised toward the associated cause')),
                ('target_date', models.DateField(help_text='The date for which the promise is expected to be redeemed')),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('cause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dps_main.Cause')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
