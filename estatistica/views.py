from decimal import Decimal
from django.views import View
from django.db.models import Avg, Count
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from math import sqrt

from estatistica.utils import Frequencia
from .models import Populacao


class IndexView(View):
    template_name = "pages/index.html"

    def get(self, request, *args, **kwargs):
        dados = {'page': 'index'}
        return render(request, self.template_name, dados)


class VisualizarPopulacaoView(View):
    template_name = "pages/populacao.html"

    def get(self, request, *args, **kwargs):
        populacao = Populacao.objects.all().order_by('id_populacao')

        pag_playoff = Paginator(populacao, 50)

        page = request.GET.get('page', 1)

        try:
            all_population = pag_playoff.page(page)
        except (EmptyPage, InvalidPage):
            all_population = pag_playoff.page(pag_playoff.num_pages)

        return render(request, self.template_name, {'populacao': all_population, 'page': 'populacao'})


class ParametrosPopulacionaisView(View):
    template_name = "pages/parametros_populacionais.html"

    def get(self, request, *args, **kwargs):
        parametros = []
        populacao_dados_a = Populacao.objects.filter(
            candidato__iexact='A').aggregate(media=Avg('idade'), qtd=Count('candidato'))

        populacao_dados_c = Populacao.objects.filter(
            candidato__iexact='C').aggregate(media=Avg('idade'), qtd=Count('candidato'))

        cand_a = Populacao.objects.filter(candidato__iexact='A').order_by('-idade')
        cand_c = Populacao.objects.filter(candidato__iexact='C').order_by('-idade')

        tabela_a = self.tabela_de_frequencia(cand_a)
        tabela_c = self.tabela_de_frequencia(cand_c)

        # print(populacao_dados[0])

        variancia_a = self.variancia(tabela_a, populacao_dados_a['media'], populacao_dados_a['qtd'] + populacao_dados_c['qtd'])
        variancia_c = self.variancia(tabela_c, populacao_dados_c['media'], populacao_dados_c['qtd'])

        total = populacao_dados_a['qtd'] + populacao_dados_c['qtd']

        desvio_padrao_a = self.desvio_padrao(variancia_a)
        desvio_padrao_c = self.desvio_padrao(variancia_c)

        tabelas = [{'candidato': 'A', 'tabela': tabela_a}, {'candidato': 'C', 'tabela': tabela_c}]

        parametros.append(
            {'candidato': 'A',
             'media': populacao_dados_a['media'],
             'total': populacao_dados_a['qtd'],
             'proporcao': (populacao_dados_a['qtd']/total) * 100,
             'variancia': variancia_a,
             'desvio_padrao': desvio_padrao_a
             }
        )

        parametros.append(
            {'candidato': 'C',
             'media': populacao_dados_c['media'],
             'total': populacao_dados_c['qtd'],
             'proporcao': (populacao_dados_c['qtd']/total) * 100,
             'variancia': variancia_c,
             'desvio_padrao': desvio_padrao_c
             }
        )

        return render(request, self.template_name, {'parametros': parametros, 'tabelas': tabelas, 'page': 'parametros'})

    def variancia(self, frequencias, media, qtd):
        soma = 0
        for f in frequencias:
            xi_x = f.xi - media
            soma += pow(xi_x, 2) * f.fi
        soma = soma / (qtd-1)
        return soma

    def desvio_padrao(self, variancia):
        return sqrt(variancia)

    def tabela_de_frequencia(self, populacao):
        list_frequencia = []
        tabela = {}
        for p in populacao:
            if p.idade in tabela:
                tabela[p.idade] += 1
            else:
                tabela[p.idade] = 1

        indice = 1
        for i in tabela:
            list_frequencia.append(Frequencia(i, tabela[i], indice))
            indice += 1

        return list_frequencia
