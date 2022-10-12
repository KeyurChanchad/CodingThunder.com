# Generated by Django 3.2.7 on 2021-09-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/blog/')),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]