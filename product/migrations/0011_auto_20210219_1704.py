# Generated by Django 3.0.7 on 2021-02-19 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210219_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(blank=True, default=2),
            preserve_default=False,
        ),
    ]
