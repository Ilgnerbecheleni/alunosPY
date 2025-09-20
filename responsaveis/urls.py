from django.urls import path
from . import views

app_name = 'responsaveis'

urlpatterns = [
    path('', views.ResponsavelListView.as_view(), name='list'),
    path('novo/', views.ResponsavelCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', views.ResponsavelUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.ResponsavelDeleteView.as_view(), name='delete'),
]
