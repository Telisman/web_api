# Generated by Django 4.1 on 2022-09-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productCode', models.CharField(max_length=15, null=True)),
                ('productName', models.CharField(max_length=70, null=True)),
                ('productLine', models.CharField(max_length=50, null=True)),
                ('productScale', models.CharField(max_length=10, null=True)),
                ('productVendor', models.CharField(max_length=50, null=True)),
                ('productDescription', models.TextField()),
                ('quantityInStock', models.IntegerField(null=True)),
                ('buyPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('MSRP', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
