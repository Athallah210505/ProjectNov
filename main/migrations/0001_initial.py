# Generated by Django 5.1.2 on 2024-10-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kartu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pengirim', models.CharField(max_length=100)),
                ('pesan', models.TextField()),
                ('wish', models.TextField()),
            ],
        ),
    ]
