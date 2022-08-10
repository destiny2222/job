from django.db import models
from django.utils.timezone import now
# Create your models here.


class Generate(models.Model):

    choice_nethod = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GPB', 'GPB'),
    ]

    fullname = models.CharField(max_length=225)
    payment_method = models.CharField(max_length=225, choices=choice_nethod)
    amount = models.DecimalField(max_digits=225, decimal_places=2)
    hashtag = models.CharField(max_length=225)
    sent_date = models.TimeField(auto_now_add=now, null=True, blank=True)

    def __str__(self):
        return self.fullname

class PaymentSlip(models.Model):
    name = models.CharField(max_length=225)
    # number = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=225, decimal_places=2)
    # sent_date = models.TimeField(default=timezone.now, null=True, blank=True)