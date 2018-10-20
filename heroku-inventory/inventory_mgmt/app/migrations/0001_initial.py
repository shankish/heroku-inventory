# Generated by Django 2.1.2 on 2018-10-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300, unique=True)),
                ('address_line_1', models.CharField(max_length=300)),
                ('address_line_2', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('pincode', models.CharField(max_length=300)),
                ('gst', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('account', models.IntegerField()),
                ('invoice_no', models.IntegerField()),
                ('invoice_no_date', models.DateField()),
                ('our_invoice_no', models.IntegerField()),
                ('our_invoice_no_date', models.DateField()),
                ('your_invoice_no', models.IntegerField()),
                ('your_invoice_no_date', models.DateField()),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sgst', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cgst', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_amount_word', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceLineItem',
            fields=[
                ('invoice_line_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_id', models.CharField(max_length=100)),
                ('particular', models.CharField(max_length=10000)),
                ('hsn_sac', models.CharField(max_length=300)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('per', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
