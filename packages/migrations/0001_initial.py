# Generated by Django 3.2 on 2023-05-20 16:45

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('package_requirements', models.TextField(default='', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=256)),
                ('equipment', models.TextField(blank=True, null=True)),
                ('duration', models.TextField(blank=True, null=True)),
                ('sensory_items_included', models.BooleanField(blank=True, default=False, null=True)),
                ('sensory_items_type', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/djck2eqxo/image/upload/v1677807568/no_package_image_mskcnk.webp', max_length=255, verbose_name='Package Image')),
                ('discount_voucher', models.DecimalField(decimal_places=1, max_digits=3)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
            options={
                'verbose_name_plural': 'Packages',
            },
        ),
    ]
