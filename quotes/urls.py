from django.urls import path

from . import views

app_name ='quotes'
urlpatterns = [
    # ex: /quotes/
    path('', views.index, name='index'),
    # ex: /quotes/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /quotes/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /quotes/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]