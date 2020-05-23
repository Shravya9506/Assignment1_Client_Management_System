from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Client, PurchasedCar
from django.urls import reverse_lazy

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PurchasedCarUpdateView(LoginRequiredMixin, UpdateView):
    model = PurchasedCar
    fields = ('soldBy', 'carName', 'carModelType', 'purchaseDate')
    template_name = 'purchasedCar_edit.html'

class PurchasedCarDeleteView(LoginRequiredMixin, DeleteView):
    model = PurchasedCar
    template_name = 'purchasedCar_delete.html'
    success_url = reverse_lazy('client_list')

class PurchasedCarCreatView(LoginRequiredMixin, CreateView):
    model = PurchasedCar
    fields = ('client', 'carName', 'carModelType', 'purchaseDate', 'soldBy')
    template_name = 'purchasedCar_new.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

