from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('citizens/', include('citizens.urls')),  # Подключение маршрутов приложения citizens
    path('cards/', include('сitizen_сards.urls')),  # Подключение маршрутов приложения citizens
    path('', lambda request: redirect('citizens:list'), name='home'),  # Редирект на список граждан
]
