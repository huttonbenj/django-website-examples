from django.apps import AppConfig


class SectionsConfig(AppConfig):
    name = 'sections'
    verbose_name = 'Home Page'
    verbose_name_plural = 'Home Page'
    def ready(self):
        import sections.signals