# Generated by Django 3.2.7 on 2021-09-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(default=''),
        ),
    ]
