# Generated by Django 3.1.2 on 2020-10-30 08:13

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0002_auto_20201022_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='strategy_parameters',
            field=jsonfield.fields.JSONField(blank=True, default={}, verbose_name='strategy parameters'),
        ),
    ]
