import hashlib
from django.db import models
from django.core.exceptions import ValidationError
from citizens.models import Citizen  # Импортируем модель Citizen из приложения citizens

# Модель CitizenCard для представления данных о банковских картах
class CitizenCard(models.Model):
    # Связь с моделью Citizen (каждая карта привязана к гражданину)
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE, related_name='cards')

    # Хранение хэшированного номера карты (PAN) для безопасности
    hash_pan = models.CharField(max_length=64, unique=True)  # Используется хэш SHA-256

    # Статус карты: активна или нет
    active = models.BooleanField(default=False)  # Если True, карта активна

    # Дата активации карты (может быть пустой, если карта не активна)
    activated_at = models.DateTimeField(null=True, blank=True)

    # Дата деактивации карты (если карта больше не активна)
    deactivated_at = models.DateTimeField(null=True, blank=True)

    def set_hash_pan(self, pan):
        """
        Устанавливает значение hash_pan на основе предоставленного PAN.
        Хэшируется PAN карты с помощью алгоритма SHA-256 для хранения в базе данных.
        """
        self.hash_pan = hashlib.sha256(pan.encode('utf-8')).hexdigest()  # Хэшируем PAN карты

    def clean(self):
        """
        Проверяет, что у гражданина может быть только одна активная карта.
        Если гражданин имеет активную карту, и пытаемся добавить новую активную, вызывается ошибка.
        """
        if self.active:
            # Проверяем, есть ли у гражданина уже активная карта
            other_active_cards = CitizenCard.objects.filter(citizen=self.citizen, active=True).exclude(id=self.id)
            if other_active_cards.exists():  # Если активная карта уже существует
                raise ValidationError('У гражданина уже есть активная карта.')
            
            # Устанавливаем дату активации для новой активной карты
            self.activated_at = models.DateTimeField(auto_now_add=True)

        # Если карта становится неактивной, устанавливаем дату деактивации
        if not self.active:
            self.deactivated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Переопределяем метод save для того, чтобы перед сохранением данных выполнить проверку.
        Вызываем clean() для проверки уникальности активной карты.
        """
        self.clean()  # Валидация перед сохранением
        super().save(*args, **kwargs)  # Сохраняем объект в базе данных

    def __str__(self):
        """
        Метод для представления объекта CitizenCard в виде строки.
        Возвращает имя и фамилию гражданина, к которому привязана карта.
        """
        return f'CitizenCard ({self.citizen.first_name} {self.citizen.last_name})'
