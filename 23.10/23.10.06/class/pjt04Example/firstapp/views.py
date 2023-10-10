from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd

plt.switch_backend('Agg')


# Create your views here.
def index(request):
    x = [1, 2, 3, 4]
    y = [2, 4, 8, 16]

    plt.clf()
    
    plt.plot(x, y)
    plt.title("Graph")
    plt.ylabel('y label')
    plt.xlabel('x label')

    buffer = BytesIO()

    plt.savefig(buffer, format='png')

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, "index.html", context)


csv_path = 'firstapp/data/austin_weather.csv'


def example(request):
    df = pd.read_csv(csv_path)
    context = {
        'df': df,
    }
    return render(request, 'example.html', context)