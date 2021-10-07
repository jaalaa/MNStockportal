from django.db import models

# Create your models here.
class JPNikkei225(models.Model):
    # # タイトル
    time = models.DateTimeField(unique_for_date=True, primary_key=True, null=False)
    # open
    open = models.FloatField(default='', )
    # close
    close = models.FloatField(default='')
    # high
    high = models.FloatField(default='', )
    # low
    low = models.FloatField(default='')
    # volume
    volume = models.IntegerField(default='', )
    # price
    price = models.FloatField(default='')

    # def value(self):
    #     return {
    #         'time': self.time,
    #         'open': self.open,
    #         'close': self.close,
    #         'high': self.high,
    #         'low': self.low,
    #         'volume': self.volume,
    #         'price': self.price,
    #     }



