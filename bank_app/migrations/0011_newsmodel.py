# Generated by Django 4.2.1 on 2023-07-11 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0010_alter_logmod1_pswd'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=3000)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]