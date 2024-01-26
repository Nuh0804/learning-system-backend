from django.apps import AppConfig


class LearningSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'learning_system'

    def ready(self):
        import learning_system.signals  # Import the module containing your signal handler