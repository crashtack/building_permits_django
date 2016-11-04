from django.apps import AppConfig


class PermitUserConfig(AppConfig):
    name = 'permit_user'
    verbose_name = 'Permit User Profile'

    def ready(self):
        """
        Code to run when the app is ready
        """
        from permit_user import handlers
