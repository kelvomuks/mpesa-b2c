# Generated by Django 2.2.4 on 2019-08-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesaApiclient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='ConversationId',
            field=models.CharField(default='drgsdr', max_length=150),
        ),
        migrations.AddField(
            model_name='response',
            name='OriginatorConversationId',
            field=models.CharField(default='drgsdryht5', max_length=150),
        ),
        migrations.AddField(
            model_name='response',
            name='ResultCode',
            field=models.IntegerField(default=2455424),
        ),
        migrations.AddField(
            model_name='response',
            name='Resulttype',
            field=models.IntegerField(default=424545),
        ),
        migrations.AddField(
            model_name='response',
            name='TransactionId',
            field=models.CharField(default='drgsd44r', max_length=150),
        ),
    ]
