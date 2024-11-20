from django.urls import path
from .views import CitizenListView, CitizenDetailView, CitizenCreateView, CitizenUpdateView

app_name = 'citizens'  # Пространство имен для маршрутов приложения

urlpatterns = [
    path('', CitizenListView.as_view(), name='list'),  # Список граждан
    path('<int:pk>/', CitizenDetailView.as_view(), name='detail'),  # Детали гражданина
    path('create/', CitizenCreateView.as_view(), name='create'),  # Создание гражданина
    path('<int:pk>/edit/', CitizenUpdateView.as_view(), name='edit'),  # Редактирование гражданина
]
