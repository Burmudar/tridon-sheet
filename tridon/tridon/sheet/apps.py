from django.apps import AppConfig


class SheetConfig(AppConfig):
    name = 'tridon.sheet'
    verbose_name = 'Sheet'

    def ready(self):
        import tridon.sheet.signals
