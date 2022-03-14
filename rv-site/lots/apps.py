from django.apps import AppConfig


class LotsConfig(AppConfig):
    name = 'lots'
    def ready(self):
        import lots.signals