# Generated by Django 3.1 on 2020-09-04 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinnerplatters',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pasta',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='regularpizza',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='salads',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='subs',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
