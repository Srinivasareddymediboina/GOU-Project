# Generated by Django 3.0.8 on 2020-07-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0031_auto_20200722_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desig',
            name='desig',
            field=models.CharField(choices=[(1, 'clerk'), (2, 'jto'), (3, 'ad'), (4, 'adet'), (5, 'adg'), (6, 'dir'), (7, 'ddg'), (8, 'other ddgs'), (9, 'srddg')], max_length=50, null=True),
        ),
    ]
