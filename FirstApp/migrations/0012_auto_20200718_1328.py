# Generated by Django 3.0.8 on 2020-07-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0011_adminfile_aplsafile_compliancefile_itfile_ruralfile_securityfile_srfile_technologyfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='typeoffile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filetype', models.CharField(choices=[('Adminfile', 'adminfile'), ('Aplsafile', 'aplsafile'), ('Compliancefile', 'compliancefile'), ('Itfile', 'itfile'), ('Ruralfile', 'ruralfile'), ('Srfile', 'srfile'), ('Securityfile', 'securityfile'), ('Technologyfile', 'technologyfile')], max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='MOU',
        ),
    ]
