from analysis.models import JPNikkei225

class DataFrameCandle(object):

    def __init__(self):
    #     self.candle_cls = factory_candle_class(self.product_code, self.duration)
        self.candles = []

    def set_all_candles(self, limit=1000):

        rawData = JPNikkei225.objects.all()

        self.candles = rawData

        # self.candles = self.candle_cls.get_all_candles(limit)
        return self.candles
        