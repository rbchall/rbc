# Generated by Django 2.1.2 on 2018-10-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_auto_20181017_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='rbcuser',
            name='first_name',
            field=models.CharField(default='firstname', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rbcuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rbcuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
