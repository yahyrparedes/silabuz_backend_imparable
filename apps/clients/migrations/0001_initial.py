# Generated by Django 4.1.2 on 2022-10-25 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commons', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('inscription_date', models.DateField(blank=True, null=True, verbose_name='inscription date')),
                ('link', models.URLField(blank=True, help_text='The url of the profile for the user', max_length=350, verbose_name='link')),
                ('picture', models.ImageField(default='images/client/avatar-default.jpeg', help_text="The url of the user's profil picture", upload_to='images/client/', verbose_name='picture')),
                ('is_kid', models.BooleanField(default=False, verbose_name='is kid')),
                ('tracklist', models.URLField(help_text='API Link to the flow of this user', max_length=350)),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(blank=True, help_text="The user's country", on_delete=django.db.models.deletion.CASCADE, to='commons.country')),
                ('gender', models.ForeignKey(blank=True, help_text="The user's gender", on_delete=django.db.models.deletion.CASCADE, to='commons.gender')),
                ('lang', models.ForeignKey(blank=True, help_text="The user's lang", on_delete=django.db.models.deletion.CASCADE, to='commons.language')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]