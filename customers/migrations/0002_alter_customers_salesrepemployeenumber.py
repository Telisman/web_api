# Generated by Django 4.1 on 2022-09-12 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='salesRepEmployeeNumber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employees'),
        ),
    ]