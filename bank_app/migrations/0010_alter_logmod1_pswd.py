# Generated by Django 4.2.1 on 2023-07-10 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0009_alter_regmod1_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmod1',
            name='pswd',
            field=models.CharField(max_length=30),
        ),
    ]
