from django.db import models

__COLS_ATTR = {'date_received': 'B',
               'consignment_id': 'D',
               'consignment_no': 'E',
               'reference': 'F',
               'return_no': 'G',
               'service_level': 'I',
               'sender': 'O',
               'consignee': 'T',
               'consignee_suburb': 'U',
               'packets': 'W',
               'kgs_used': 'AB',
               'rate_per_kg': 'AG',
               'min_charge': 'AI',
               'doc_fee': 'AJ',
               'fuel_surcharge': 'BJ',
               'amount': 'BM'}

def get_col_for_attr(attr):
    if attr not in __COLS_ATTR:
        raise KeyError("No Matching column found for attribute '{}'".format(attr))
    return __COLS_ATTR[attr]


class WorkbookFile(models.Model):

    file = models.FileField('Path to Spreadsheet', upload_to='sheet_uploads/')
    file_hash = models.TextField(unique=True, max_length=256, editable=False)
    created = models.DateTimeField('Date Uploaded', editable=False, auto_now=True)


class WorkbookEntry(models.Model):

    date_received = models.DateTimeField('Date Received', editable=False)
    consignment_id = models.CharField('Consignment ID', max_length=20)
    consignment_no = models.CharField('Consignment No', max_length=20)
    reference = models.CharField('Reference #1', max_length=255)
    return_no = models.CharField('Return No', max_length=30)
    service_level = models.IntegerField("Service Level")
    sender = models.CharField('Sender Name', max_length=255)
    consignee = models.CharField('Consignee Name', max_length=50)
    consignee_suburb = models.CharField('Consignee suburb', max_length=50)
    packets = models.IntegerField('Packets')
    kgs_used = models.DecimalField('Kgs Used', max_digits=10, decimal_places=2)
    rate_per_kg = models.DecimalField('Rate Per Kg', max_digits=10, decimal_places=2)
    min_charge = models.DecimalField('Minimum Charge', max_digits=10, decimal_places=2)
    doc_fee = models.DecimalField('Document Fee', max_digits=10, decimal_places=2)
    fuel_surcharge = models.DecimalField('Fuel Surchare Ex. Vat', max_digits=10, decimal_places=2)
    amount = models.DecimalField('Amount incl. VAT', max_digits=10, decimal_places=2)

    def __eq__(self, other):
        if super(self, other):
            return self.__dict__ == other.__dict__
        return False

    def is_empty(self):
        return self.date_received == ''
