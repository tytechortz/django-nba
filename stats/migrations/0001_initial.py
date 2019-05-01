# Generated by Django 2.2 on 2019-05-01 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('fullname', models.CharField(max_length=30)),
                ('tricode', models.CharField(max_length=3)),
                ('teamId', models.CharField(max_length=10)),
                ('nickname', models.CharField(max_length=20)),
                ('confName', models.CharField(max_length=4)),
                ('divName', models.CharField(max_length=10)),
                ('photo_url', models.TextField()),
            ],
        ),
    ]
