# Generated by Django 2.2.4 on 2019-08-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesaApiclient', '0003_auto_20190819_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b2cresponse',
            name='ResultCode',
            field=models.CharField(default='24yhjy55424', max_length=150),
        ),
        migrations.AlterField(
            model_name='b2cresponse',
            name='Resulttype',
            field=models.CharField(default='rt6uy424545', max_length=150),
        ),
    ]
