from django.db import models


class WorkbookFile(models.Model):

    path = models.FileField('Path to Spreadsheet', upload_to='sheet_uploads/')
    file_hash = models.TextField(unique=True, max_length=256, editable=False)
    created = models.DateTimeField('Date Uploaded', editable=False, auto_now=True)


class WorkbookEntry(models.Model):
    date_received = models.DateTimeField('Date Received', editable=False)
    consignment_id = models.CharField('Consignment ID', max_length=20)
    consignment_no = models.CharField('Consignment No', max_length=20)
    reference = models.CharField('Reference #1', max_length=30)
    return_no = models.CharField('Return No', max_length=30)
    sender = models.CharField('Sender Name', max_length=30)
    consignee = models.CharField('Consignee Name', max_length=50)
    consignee_suburb = models.CharField('Consignee suburb', max_length=50)
    packets = models.IntegerField('Packets')
    kgs_used = models.DecimalField('Kgs Used', max_digits=10, decimal_places=2)
    rate_per_kg = models.DecimalField('Rate Per Kg', max_digits=10, decimal_places=2)
    min_charge = models.DecimalField('Minimum Charge', max_digits=10, decimal_places=2)
    doc_fee = models.DecimalField('Document Fee', max_digits=10, decimal_places=2)
    fuel_surcharge = models.DecimalField('Fuel Surchare Ex. Vat', max_digits=10, decimal_places=2)
    amount = models.DecimalField('Amount incl. VAT', max_digits=10, decimal_places=2)
