# Generated by Django 4.1.1 on 2022-09-25 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('logo', models.ImageField(default='no_picture.png', upload_to='customers')),
            ],
        ),
    ]
