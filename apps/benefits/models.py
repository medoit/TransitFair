# apps/benefits/models.py
from django.db import models  # Импортируем модуль моделей из Django
from citizens.models import Citizen  # Импортируем модель Citizen для создания связи

# Определяем модель Benefit для представления данных о льготах
class Benefit(models.Model):
    # Поле для названия льготы, ограниченное 200 символами
    name = models.CharField(max_length=200)

    # Поле для описания льготы (может быть пустым или равным NULL)
    description = models.TextField(blank=True, null=True)

    # Связь с моделью Citizen через внешний ключ
    # Если связанный гражданин удаляется, все связанные с ним льготы также удаляются (CASCADE)
    citizen = models.ForeignKey(
        Citizen, 
        on_delete=models.CASCADE, 
        related_name="benefits"  # Позволяет обращаться к льготам гражданина через `citizen.benefits.all()`
    )

    # Поле для хранения уникального Hash-PAN карты (например, хэшированного номера карты льготы)
    hash_pan = models.CharField(max_length=64, unique=True)

    # Поле, автоматически устанавливающее дату и время создания записи
    created_at = models.DateTimeField(auto_now_add=True)

    # Метод для текстового представления объекта Benefit
    def __str__(self):
        # Возвращаем строку с названием льготы и данными о гражданине
        return f"{self.name} ({self.citizen})"
