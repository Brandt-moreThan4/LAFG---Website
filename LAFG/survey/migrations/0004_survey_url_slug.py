# Generated by Django 3.1 on 2021-03-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20210308_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='url_slug',
            field=models.SlugField(default='bet', max_length=300),
            preserve_default=False,
        ),
    ]
