# Generated by Django 5.0.6 on 2024-07-07 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardekho_app', '0002_carlist_chassisnumber_carlist_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showroomlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('website', models.URLField(max_length=100)),
            ],
        ),
    ]
