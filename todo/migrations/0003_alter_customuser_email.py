# Generated by Django 5.2.3 on 2025-07-14 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
