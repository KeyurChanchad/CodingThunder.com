# Generated by Django 3.2.7 on 2021-12-20 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='view',
        ),
    ]