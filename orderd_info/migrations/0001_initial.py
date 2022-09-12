# Generated by Django 4.1 on 2022-09-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orderd_info',
            fields=[
                ('orderd_info_id', models.AutoField(primary_key=True, serialize=False)),
                ('orderNumber', models.IntegerField(blank=True, null=True)),
                ('productCode', models.CharField(max_length=15, null=True)),
                ('quantityOrdered', models.IntegerField(blank=True, null=True)),
                ('orderLineNumber', models.IntegerField(blank=True, null=True)),
                ('priceEach', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
