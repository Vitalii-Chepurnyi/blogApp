# Generated by Django 4.2.8 on 2024-01-01 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]