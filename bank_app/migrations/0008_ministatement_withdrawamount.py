# Generated by Django 4.2.1 on 2023-07-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0007_rename_addamount_addamount_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ministatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.IntegerField(choices=[('withdraw', 'withdraw'), ('deposit', 'deposit')])),
            ],
        ),
        migrations.CreateModel(
            name='withdrawamount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
