from django.urls import path

from . import views

#для определения псевдоминов, чтобы django не путался
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/add_comment', views.add_comment, name='add_comment'),
    #path('test', views.test, name='test')
]