from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Responsavel
from .forms import ResponsavelForm

class ResponsavelListView(LoginRequiredMixin, ListView):
    model = Responsavel
    template_name = 'responsaveis/responsaveis_list.html'
    context_object_name = 'responsaveis'
    paginate_by = 10

class ResponsavelCreateView(LoginRequiredMixin, CreateView):
    model = Responsavel
    form_class = ResponsavelForm
    template_name = 'responsaveis/responsaveis_form.html'
    success_url = reverse_lazy('responsaveis:list')
    def form_valid(self, form):
        messages.success(self.request, "Responsável criado com sucesso!")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "Corrija os erros abaixo.")
        return super().form_invalid(form)

class ResponsavelUpdateView(LoginRequiredMixin, UpdateView):
    model = Responsavel
    form_class = ResponsavelForm
    template_name = 'responsaveis/responsaveis_form.html'
    success_url = reverse_lazy('responsaveis:list')
    def form_valid(self, form):
        messages.success(self.request, "Responsável atualizado com sucesso!")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "Corrija os erros abaixo.")
        return super().form_invalid(form)

class ResponsavelDeleteView(LoginRequiredMixin, DeleteView):
    model = Responsavel
    template_name = 'responsaveis/responsaveis_confirm_delete.html'
    success_url = reverse_lazy('responsaveis:list')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Responsável excluído com sucesso!")
        return super().delete(request, *args, **kwargs)
