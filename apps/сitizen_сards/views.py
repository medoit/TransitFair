# views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import CitizenCard, Citizen
from django.urls import reverse_lazy

class CitizenCardListView(ListView):
    model = CitizenCard
    template_name = 'сitizen_сards/citizen_card_list.html'
    context_object_name = 'cards'

class CitizenCardDetailView(DetailView):
    model = CitizenCard
    template_name = 'сitizen_сards/citizen_card_detail.html'
    context_object_name = 'card'

class CitizenCardCreateView(CreateView):
    model = CitizenCard
    template_name = 'сitizen_сards/citizen_card_create.html'
    fields = ['citizen', 'hash_pan', 'active']
    success_url = reverse_lazy('citizen_card_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['citizens'] = Citizen.objects.all()  # Передаем всех граждан для выбора
        return context
