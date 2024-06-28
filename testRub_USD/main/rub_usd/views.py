from django.shortcuts import render
from django.http import JsonResponse
import time
import requests
from .models import CurrencyRateLog
def get_current_usd(request):
    # Запрос к API для получения курса доллара к рублю
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    usd_rate = data['rates']['RUB']

    # Сохранение курса в базу данных
    CurrencyRateLog.objects.create(rate=usd_rate)

    # Получение последних 10 запросов курсов
    rates_logs = CurrencyRateLog.objects.order_by('-timestamp')[:10]

    rates_history = [{'rate': log.rate, 'timestamp': log.timestamp} for log in rates_logs]

    # Пауза перед отправкой ответа не менее 10 секунд
    time.sleep(10)

    return JsonResponse({'current_usd_rate': usd_rate, 'rates_history': rates_history})