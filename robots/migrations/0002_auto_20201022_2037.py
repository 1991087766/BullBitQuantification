# Generated by Django 3.1.2 on 2020-10-22 12:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='enabled',
            field=models.BooleanField(default=False, verbose_name='enabled'),
        ),
        migrations.CreateModel(
            name='AssetRecordSnap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('modified_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified_at')),
                ('total_principal', models.FloatField(verbose_name='total capital')),
                ('total_balance', models.FloatField(verbose_name='total balance')),
                ('period', models.CharField(choices=[('1h', '1 hour'), ('1d', '1 day')], max_length=10, verbose_name='period')),
                ('asset_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snaps', to='robots.assetrecord', verbose_name='asset record')),
            ],
            options={
                'verbose_name': 'asset record snap',
                'verbose_name_plural': 'asset record snaps',
            },
        ),
    ]
