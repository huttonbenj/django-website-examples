from django.apps import AppConfig


class SpecialsConfig(AppConfig):
    name = 'specials'
    def ready(self):
        import specials.signals