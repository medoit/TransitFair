from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Citizen
from .forms import CitizenForm

# Класс для отображения списка граждан
class CitizenListView(ListView):
    model = Citizen
    template_name = 'citizens/citizen_list.html'  # Путь к шаблону
    context_object_name = 'citizens'  # Имя переменной в шаблоне
    paginate_by = 10  # Количество записей на страницу (опционально)

# Класс для отображения деталей конкретного гражданина
class CitizenDetailView(DetailView):
    model = Citizen
    template_name = 'citizens/citizen_detail.html'
    context_object_name = 'citizen'
    
    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст
        context = super().get_context_data(**kwargs)
        
        # Добавляем карты гражданина в контекст
        citizen = context[self.context_object_name]  # Получаем объект гражданина из контекста
        context['cards'] = citizen.cards.all()  # Получаем все карты, связанные с этим гражданином
        
        return context

# Класс для создания нового гражданина
class CitizenCreateView(CreateView):
    model = Citizen
    form_class = CitizenForm  # Форма для создания гражданина
    template_name = 'citizens/citizen_form.html'
    success_url = reverse_lazy('citizens:list')  # Перенаправление после успешного создания

# Класс для редактирования данных гражданина
class CitizenUpdateView(UpdateView):
    model = Citizen
    form_class = CitizenForm
    template_name = 'citizens/citizen_form.html'
    success_url = reverse_lazy('citizens:list')  # Перенаправление после успешного обновления
