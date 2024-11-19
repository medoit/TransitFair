# apps/citizens/models.py
from django.db import models  # Импортируем модуль моделей из Django

# Определяем модель Citizen для представления данных о гражданах
class Citizen(models.Model):
    # Поле для имени гражданина, ограниченное 100 символами
    first_name = models.CharField(max_length=100)

    # Поле для фамилии гражданина, ограниченное 100 символами
    last_name = models.CharField(max_length=100)

    # Поле для даты рождения гражданина
    birth_date = models.DateField()

    # Уникальное поле для идентификации гражданина (например, номер паспорта)
    citizen_id = models.CharField(max_length=50, unique=True)

    # Поле, автоматически устанавливающее дату и время создания записи
    created_at = models.DateTimeField(auto_now_add=True)

    # Метод для текстового представления объекта Citizen
    def __str__(self):
        # Возвращаем строку с именем, фамилией и уникальным ID гражданина
        return f"{self.first_name} {self.last_name} ({self.citizen_id})"
