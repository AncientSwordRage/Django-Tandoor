from django.db import models
from decimal import Decimal
class CurrencyField(models.DecimalField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, currency_symbol='£', *args, **kwargs):
        super(CurrencyField, self).__init__(*args, **kwargs)
        self.currency_symbol = currency_symbol
        if(len(self.currency_symbol) != 1):
        	raise ValueError("Currency Symbol must be one character")

    def to_python(self, value):
        try:
           return super(CurrencyField, self).to_python(value).quantize(Decimal("0.01"))
        except AttributeError:
           return None
