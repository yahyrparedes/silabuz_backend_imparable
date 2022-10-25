# Generated by Django 4.1.2 on 2022-10-25 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_alter_artist_link_alter_artist_nb_album_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='nb_album',
            field=models.IntegerField(blank=True, help_text="The number of artist's albums"),
        ),
        migrations.AlterField(
            model_name='artist',
            name='nb_fan',
            field=models.IntegerField(blank=True, help_text="The number of artist's fans"),
        ),
    ]