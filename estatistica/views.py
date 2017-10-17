from django.views import View
from django.shortcuts import render


class IndexView(View):
    template_name = "pages/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class DadosIniciais(View):
    template_name = "pages/dados_iniciais.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
