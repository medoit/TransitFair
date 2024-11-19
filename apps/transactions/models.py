# apps/transactions/models.py
from django.db import models  # Импортируем модуль моделей из Django
from benefits.models import Benefit  # Импортируем модель Benefit для связи

# Определяем модель Transaction для представления данных о транзакциях
class Transaction(models.Model):
    # Варианты статусов транзакции
    TRANSACTION_STATUS_CHOICES = [
        ('SUCCESS', 'Successful'),  # Успешная транзакция
        ('FAILED', 'Failed'),  # Неудачная транзакция
        ('DISCOUNT_ERROR', 'Discount Error'),  # Ошибка при расчёте скидки
    ]

    # Поле для Hash-PAN карты, связанное с Benefit через значение hash_pan
    hash_pan = models.CharField(max_length=64)

    # Поле для времени выполнения транзакции
    transaction_time = models.DateTimeField()

    # Поле для суммы транзакции с двумя знаками после запятой
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Поле для идентификатора терминала, где была выполнена транзакция
    terminal_id = models.CharField(max_length=100)

    # Поле для статуса транзакции, с выбором из предопределённых вариантов
    status = models.CharField(
        max_length=20, 
        choices=TRANSACTION_STATUS_CHOICES,  # Список допустимых значений
        default='SUCCESS'  # Значение по умолчанию
    )

    # Поле, автоматически устанавливающее дату и время создания записи
    created_at = models.DateTimeField(auto_now_add=True)

    # Метод для текстового представления объекта Transaction
    def __str__(self):
        # Возвращаем строку с Hash-PAN карты и статусом транзакции
        return f"Transaction {self.hash_pan} - {self.status}"
