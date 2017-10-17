from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(email="marlonbquadros@gmail.com.br").exists():
            User.objects.create_superuser("marlon@doshiapp.com.br", "marlon@doshiapp.com.br", "MaR111990")
