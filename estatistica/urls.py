from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^populacao/$', views.VisualizarPopulacaoView.as_view()),
    url(r'^parametros/$', views.ParametrosPopulacionaisView.as_view()),
]
