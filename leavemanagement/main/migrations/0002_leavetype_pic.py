# Generated by Django 2.1.4 on 2019-02-16 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavetype',
            name='pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
