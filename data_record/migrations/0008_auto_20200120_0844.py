# Generated by Django 3.0.1 on 2020-01-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_record', '0007_auto_20200120_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='person',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
