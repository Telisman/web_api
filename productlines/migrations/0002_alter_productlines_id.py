# Generated by Django 4.1 on 2022-09-13 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlines',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]