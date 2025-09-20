from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from .models import Aluno
from .forms import AlunoForm

class AlunoListView(LoginRequiredMixin, ListView):
    model = Aluno
    template_name = 'alunos/alunos_list.html'
    context_object_name = 'alunos'
    paginate_by = 10

class AlunoCreateView(LoginRequiredMixin, CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'alunos/alunos_form.html'
    success_url = reverse_lazy('alunos:list')
    def form_valid(self, form):
        messages.success(self.request, "Aluno criado com sucesso!")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "Corrija os erros abaixo.")
        return super().form_invalid(form)

class AlunoUpdateView(LoginRequiredMixin, UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'alunos/alunos_form.html'
    success_url = reverse_lazy('alunos:list')
    def form_valid(self, form):
        messages.success(self.request, "Aluno atualizado com sucesso!")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "Corrija os erros abaixo.")
        return super().form_invalid(form)

class AlunoDeleteView(LoginRequiredMixin, DeleteView):
    model = Aluno
    template_name = 'alunos/alunos_confirm_delete.html'
    success_url = reverse_lazy('alunos:list')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Aluno excluído com sucesso!")
        return super().delete(request, *args, **kwargs)
