# Generated by Django 5.1.2 on 2024-10-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
