# Generated by Django 2.1.2 on 2018-10-23 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_remove_aaa_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='aaa',
            name='priority',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]