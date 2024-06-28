from django.db import models

class CurrencyRateLog(models.Model):
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)