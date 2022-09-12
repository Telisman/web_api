# Generated by Django 4.1 on 2022-09-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customerNumber', models.AutoField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=100, null=True)),
                ('contactLastName', models.CharField(max_length=100, null=True)),
                ('contactFirstName', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('addressLine1', models.CharField(max_length=100, null=True)),
                ('addressLine2', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('postalCode', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('salesRepEmployeeNumber', models.IntegerField(blank=True, null=True)),
                ('creditLimit', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]