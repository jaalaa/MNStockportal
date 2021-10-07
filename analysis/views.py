from django.shortcuts import render
from django.contrib import messages
from analysis.models import JPNikkei225
from analysis.candle import DataFrameCandle

from django.http import JsonResponse


def index(request):

    objs = JPNikkei225.objects.all()

    context = {
        'nikkei' : objs
    }

    # context = {
    # }

    return render(request, 'analysis/index.html', context)


def api_make_handler(request):

    product_code = request.GET.get('product_code')

    print('---------',product_code)

    if not product_code:
        return JsonResponse({'error': 'No product_code params'}), 400

    limit_str = request.GET.get('limit')
    limit = 1000
    if limit_str:
        limit = int(limit_str)

    if limit < 0 or limit > 1000:
        limit = 1000

    duration = request.GET.get('duration')
    
    df = DataFrameCandle()
    df.set_all_candles()

    for obj in df:
        print('---------',obj)

        
   
    # print('--------',df.value )

    # return JsonResponse(df.value)
    return render(request, 'analysis/index.html', {})
