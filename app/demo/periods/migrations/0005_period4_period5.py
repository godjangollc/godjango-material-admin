# Generated by Django 3.0 on 2019-12-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periods', '0004_period1_period2_period3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=255, verbose_name='Period4')),
            ],
            options={
                'verbose_name': 'Period4',
                'verbose_name_plural': 'Periods4',
            },
        ),
        migrations.CreateModel(
            name='Period5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=255, verbose_name='Period5')),
            ],
            options={
                'verbose_name': 'Period5',
                'verbose_name_plural': 'Periods5',
            },
        ),
    ]