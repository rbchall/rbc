# Generated by Django 2.1.2 on 2018-10-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20181022_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='Description_for_seo',
            field=models.TextField(blank=True, help_text='Decription of page for seo', max_length=255, null=True),
        ),
    ]