# Generated by Django 4.2.1 on 2023-07-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0013_withdrawamount_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='tablesmod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=30)),
            ],
        ),
    ]