# Generated by Django 3.1 on 2021-03-20 22:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_auto_20210320_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey_record',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
