# Generated by Django 4.1 on 2022-09-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id_payments', models.AutoField(primary_key=True, serialize=False)),
                ('customerNumber', models.IntegerField(blank=True, null=True)),
                ('checkNumber', models.CharField(max_length=50, null=True)),
                ('paymentDate', models.DateField(null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
