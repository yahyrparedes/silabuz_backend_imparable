# Generated by Django 4.1.2 on 2022-10-25 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_alter_client_country_alter_client_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='inscription_date',
        ),
    ]