from django.apps import AppConfig


class AnnotationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'annotation'

    def ready(self) -> None:
        import annotation.signals
