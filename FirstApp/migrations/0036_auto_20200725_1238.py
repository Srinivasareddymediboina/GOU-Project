# Generated by Django 3.0.8 on 2020-07-25 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0035_auto_20200725_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desig',
            name='notify',
        ),
        migrations.AddField(
            model_name='documentuserdata',
            name='notify',
            field=models.IntegerField(default=0, null=True),
        ),
    ]