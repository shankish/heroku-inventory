from django.contrib import admin
from app.models import *

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_id' ,'name']

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_id', 'account']

class InvoiceLineItemAdmin(admin.ModelAdmin):
    list_display = ['invoice_line_item_id','invoice_id']

admin.site.register(Account, AccountAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceLineItem, InvoiceLineItemAdmin)