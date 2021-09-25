from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='predict/indexbase.html'), name="index"),

    path('supervised', views.index, name='supervised'),
    path('result/', views.result, name='result'),
    path('unsupervised/visualization/base_lda/tsne/', TemplateView.as_view(template_name="predict/lda_base_tsne.html"), name="base_tsne"),
    path('unsupervised/visualization/base_lda/mmds/', TemplateView.as_view(template_name="predict/lda_base_mmds.html"), name="base_mmds"),
    path('unsupervised/visualization/base_lda/pcoa/', TemplateView.as_view(template_name="predict/lda_base_pcoa.html"), name="base_pcoa"),

    path('unsupervised/visualization/bigram_lda/tsne/', TemplateView.as_view(template_name="predict/lda_tsne.html"), name="bigram_tsne"),
    path('unsupervised/visualization/bigram_lda/mmds/', TemplateView.as_view(template_name="predict/lda_mmds.html"), name="bigram_mmds"),
    path('unsupervised/visualization/bigram_lda/pcoa/', TemplateView.as_view(template_name="predict/lda_pcoa.html"), name="bigram_pcoa"),
    path('unsupervised/visualization/gsdmm/plotly/', TemplateView.as_view(template_name="predict/plotly_topics.html"), name="topics"),
    path('unsupervised/', TemplateView.as_view(template_name='predict/unsupervised_index.html'), name="unsupervised"),
    path('resources/', TemplateView.as_view(template_name="predict/resources.html"), name='resources'),

]