# Generated by Django 4.0 on 2023-07-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('guardianfirstname', models.CharField(max_length=255)),
                ('guardianlastname', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('entrynumber', models.CharField(max_length=12)),
                ('department', models.CharField(max_length=5)),
                ('hostel', models.CharField(max_length=20)),
                ('roomnumber', models.CharField(max_length=10)),
                ('emergencynumber', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('swim', models.CharField(max_length=1)),
            ],
        ),
    ]