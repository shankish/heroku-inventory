from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, unique=True)
    address_line_1 = models.CharField(max_length=300)
    address_line_2 = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    pincode = models.CharField(max_length=300)
    gst = models.CharField(max_length=10, unique=True)

class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    account = models.IntegerField()
    invoice_no = models.IntegerField()
    invoice_no_date = models.DateField()
    our_invoice_no = models.IntegerField() 
    our_invoice_no_date = models.DateField() 
    your_invoice_no = models.IntegerField()
    your_invoice_no_date = models.DateField()
    sub_total = models.DecimalField(decimal_places=2,max_digits=8)
    sgst = models.DecimalField(decimal_places=2,max_digits=8)
    cgst = models.DecimalField(decimal_places=2,max_digits=8)
    total_amount = models.DecimalField(decimal_places=2,max_digits=8)
    total_amount_word = models.CharField(max_length=300)

class InvoiceLineItem(models.Model):
    invoice_line_item_id = models.AutoField(primary_key=True)
    invoice_id = models.CharField(max_length=100)
    particular = models.CharField(max_length=10000)
    hsn_sac = models.CharField(max_length=300)
    quantity = models.DecimalField(decimal_places=2,max_digits=8)
    rate = models.DecimalField(decimal_places=2,max_digits=8)
    per = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2,max_digits=8)