# Generated by Django 3.1 on 2020-09-04 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200904_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regularpizza',
            name='toppings',
            field=models.ManyToManyField(to='orders.Toppings'),
        ),
    ]
