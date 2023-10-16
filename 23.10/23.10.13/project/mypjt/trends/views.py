from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm
from bs4 import BeautifulSoup
from selenium import webdriver
from django.utils import timezone
import matplotlib.pyplot as plt
from io import BytesIO
import base64

plt.switch_backend('Agg')

# Create your views here.
def index(request):
    return render(request, 'trends/base.html')


def keyword(request):
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if Keyword.objects.filter(name=request.POST['name']):
            return redirect('trends:keyword')
        
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    else:
        form = KeywordForm()

    keyword_querysets = Keyword.objects.all()
    sequence = 1
    keywords = []

    for keyword_queryset in keyword_querysets:
        keywords.append([sequence, keyword_queryset])
        sequence += 1

    context = {
        'form': form,
        'keywords': keywords,
    }

    return render(request, 'trends/keyword.html', context)


def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword_name = keyword.name
    trends = Trend.objects.filter(name=keyword_name)
    keyword.delete()
    for trend in trends:
        trend.delete()

    return redirect('trends:keyword')


def crawling(request):
    keywords = Keyword.objects.all()
    driver = webdriver.Chrome()
    for keyword in keywords:
        url = f'https://www.google.com/search?q={keyword.name}'
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        result_stats_soup = soup.select_one('div#result-stats')

        if result_stats_soup:
            result_stats = result_stats_soup.text
        else:
            continue

        from_index = result_stats.index("약")
        to_index = result_stats.index("개")
        
        result = ""
        
        for index in range(from_index + 2, to_index):
            if result_stats[index] == ",":
                continue
            
            result += result_stats[index]

        trend_with_name = Trend.objects.filter(name=keyword.name, search_period="all")
        
        if len(trend_with_name) == 1:
            for trend in trend_with_name:
                trend.result = int(result)
                trend.created_at = timezone.now()
                trend.save()
        else:
            trend = Trend(name=keyword.name, result=int(result), search_period="all", created_at=timezone.now())
            trend.save()
    
    trends = Trend.objects.filter(search_period="all")

    context = {
        'trends': trends,
    }
        
    return render(request, 'trends/crawling.html', context)


def crawling_histogram(request):
    trends = Trend.objects.all()
    plt.clf()

    x = []
    y = []

    for trend in trends:
        x.append(trend.name)
        y.append(trend.result)
    
    plt.figure(figsize=(10, 5))
    plt.bar(x, y, label='Trends')
    plt.legend()
    plt.grid()
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'trends/crawling_histogram.html', context)


def crawling_advanced(request):
    keywords = Keyword.objects.all()
    driver = webdriver.Chrome()
    for keyword in keywords:
        url = f'https://www.google.com/search?q={keyword.name}&tbs=qdr:y'
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        result_stats_soup = soup.select_one('div#result-stats')

        if result_stats_soup:
            result_stats = result_stats_soup.text
        else:
            continue

        from_index = result_stats.index("약")
        to_index = result_stats.index("개")
        
        result = ""
        
        for index in range(from_index + 2, to_index):
            if result_stats[index] == ",":
                continue
            
            result += result_stats[index]

        trend_with_name = Trend.objects.filter(name=keyword.name, search_period="year")
        
        if len(trend_with_name) == 1:
            for trend in trend_with_name:
                trend.result = int(result)
                trend.created_at = timezone.now()
                trend.save()
        else:
            trend = Trend(name=keyword.name, result=int(result), search_period="year", created_at=timezone.now())
            trend.save()
    
    trends = Trend.objects.filter(search_period="year")

    plt.clf()

    x = []
    y = []

    for trend in trends:
        x.append(trend.name)
        y.append(trend.result)
    
    plt.figure(figsize=(10, 5))
    plt.bar(x, y, label='Trends')
    plt.legend()
    plt.grid()
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'trends/crawling_advanced.html', context)
