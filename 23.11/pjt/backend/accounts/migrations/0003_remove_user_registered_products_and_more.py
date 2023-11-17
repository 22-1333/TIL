# Generated by Django 4.2.7 on 2023-11-17 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_registered_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='registered_products',
        ),
        migrations.AddField(
            model_name='user',
            name='registered_products',
            field=models.TextField(blank=True, null=True),
        ),
    ]
