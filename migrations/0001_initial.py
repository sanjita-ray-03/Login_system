# Generated by Django 5.0.3 on 2024-03-15 14:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9a-zA-z]*$', 'Only alphanumeric characters are allowed')])),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100, validators=[django.core.validators.RegexValidator('^[0-9a-zA-z]*$', 'Only alphanumeric characters are allowed')])),
                ('password', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9a-zA-z]*$', 'Only alphanumeric characters are allowed')])),
            ],
        ),
    ]
