# Generated by Django 2.1.4 on 2019-02-16 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_leavetype_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='model1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('sal', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='model2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='proxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('main.model2',),
        ),
    ]
