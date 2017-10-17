import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from estatistica.models import Populacao

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(os.path.join('estatistica', 'management', 'commands', 'Trabalho_T2.csv'), 'r') as file:
            linhas = file.readlines()
            for l in range(1, len(linhas)):
                linha = linhas[l].split(';')
                if len(linha) > 2:
                    Populacao.objects.create(id_populacao=linha[0], idade=linha[1],
                                             candidato=linha[2].replace('\n', ''))

            self.stdout.write(self.style.SUCCESS('População adicionada com sucesso'))
