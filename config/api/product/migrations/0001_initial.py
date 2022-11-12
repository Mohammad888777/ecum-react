# Generated by Django 4.1.3 on 2022-11-11 10:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('stock', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ProductIMG', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['img', 'png', 'jpeg'])])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category')),
            ],
        ),
    ]
