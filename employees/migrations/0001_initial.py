# Generated by Django 4.1 on 2022-09-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employeeNumber', models.AutoField(primary_key=True, serialize=False)),
                ('lastName', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('extension', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('officeCode', models.IntegerField(null=True)),
                ('reportsTo', models.IntegerField(null=True)),
                ('jobTitle', models.CharField(max_length=100)),
            ],
        ),
    ]
