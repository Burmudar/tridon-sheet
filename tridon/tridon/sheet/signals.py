from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import WorkbookFile
# Create your models here.


@receiver(pre_save, sender=WorkbookFile)
def hash_sheet(sender, **kwargs):
    pass
