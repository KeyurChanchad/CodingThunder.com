# Generated by Django 3.2.7 on 2021-12-20 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]