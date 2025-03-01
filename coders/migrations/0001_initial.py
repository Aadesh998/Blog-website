# Generated by Django 4.2 on 2023-08-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Desc', models.TextField()),
                ('author', models.CharField(max_length=130)),
                ('image', models.ImageField(upload_to='images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.CharField(max_length=300)),
            ],
        ),
    ]
