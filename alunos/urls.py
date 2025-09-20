from django.urls import path
from . import views

app_name = 'alunos'

urlpatterns = [
    path('', views.AlunoListView.as_view(), name='list'),
    path('novo/', views.AlunoCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', views.AlunoUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.AlunoDeleteView.as_view(), name='delete'),
]
