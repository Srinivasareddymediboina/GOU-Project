# Generated by Django 3.0.8 on 2020-07-25 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0033_auto_20200723_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='desig',
            name='notify',
            field=models.IntegerField(null=True),
        ),
    ]