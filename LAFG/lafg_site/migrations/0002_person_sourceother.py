# Generated by Django 3.1 on 2020-09-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lafg_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='sourceOther',
            field=models.CharField(default='Blank', max_length=250),
            preserve_default=False,
        ),
    ]
