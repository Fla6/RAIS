# Generated by Django 3.0.4 on 2020-11-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rais', '0006_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='town',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
