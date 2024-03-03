# Generated by Django 4.0.3 on 2024-02-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=200, unique=True)),
                ('Types', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('address', models.TextField()),
                ('phone', models.IntegerField(unique=True)),
                ('product', models.TextField()),
                ('quantity', models.IntegerField()),
                ('amount', models.TextField()),
                ('invoiceNumber', models.IntegerField()),
                ('invoiceDate', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('address', models.TextField()),
                ('phone', models.IntegerField(unique=True)),
                ('salary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('colorname', models.CharField(max_length=200, unique=True)),
                ('Category', models.CharField(max_length=100)),
                ('Brand', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Items', models.CharField(max_length=100, unique=True)),
                ('category', models.CharField(max_length=100, unique=True)),
                ('Brand', models.CharField(max_length=100, unique=True)),
                ('Status', models.CharField(max_length=100)),
                ('sellingprice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppliercode', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.TextField()),
                ('phone', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
    ]