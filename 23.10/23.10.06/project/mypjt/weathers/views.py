from django.shortcuts import render, redirect
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np
from .models import Reply
from .forms import ReplyForm

df = pd.read_csv('weathers/data/austin_weather.csv')
df = df.astype({'TempHighF':'int', 'TempAvgF':'int', 'TempLowF':'int'})
plt.switch_backend('Agg')

# Create your views here.
def index(request):
    return render(request, 'base.html')


def problem(request, num):
    if num == 1:
        replies = Reply.objects.all()
        context = {
            'problem_num': 1,
            'df': df,
            'replies': replies,
        }
        return render(request, 'problem1.html', context)
    
    elif num == 2:
        plt.clf()

        x = pd.to_datetime(df['Date'])
        y1 = df['TempHighF']
        y2 = df['TempAvgF']
        y3 = df['TempLowF']

        plt.figure(figsize=(10, 5))
        plt.plot(x, y1, label='High Temperature')
        plt.plot(x, y2, label='Average Temperature')
        plt.plot(x, y3, label='Low Temperature')
        plt.legend(loc='lower center')
        plt.grid()
        plt.title('Temperature Variation')
        plt.xlabel('Date')
        plt.ylabel('Temperature (Fahrenheit)')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
        buffer.close()

        replies = Reply.objects.all()
        context = {
            'problem_num': 2,
            'chart_image': f'data:image/png;base64,{image_base64}',
            'replies': replies,
        }

        return render(request, 'problem2.html', context)

    elif num == 3:
        plt.clf()

        df_problem3 = df[['Date', 'TempHighF', 'TempAvgF', 'TempLowF']]
        df_problem3['Date'] = pd.to_datetime(df_problem3['Date'])

        df_monthly = df_problem3.groupby(by=df_problem3['Date'].dt.strftime("%Y-%m")).mean()

        x = df_monthly['Date']
        y1 = df_monthly['TempHighF']
        y2 = df_monthly['TempAvgF']
        y3 = df_monthly['TempLowF']

        plt.figure(figsize=(10, 5))
        plt.plot(x, y1, label='High Temperature')
        plt.plot(x, y2, label='Average Temperature')
        plt.plot(x, y3, label='Low Temperature')
        plt.legend(loc='lower right')
        plt.grid()
        plt.title('Temperature Variation')
        plt.xlabel('Date')
        plt.ylabel('Temperature (Fahrenheit)')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
        buffer.close()

        replies = Reply.objects.all()
        context = {
            'problem_num': 3,
            'chart_image': f'data:image/png;base64,{image_base64}',
            'replies': replies,
        }

        return render(request, 'problem3.html', context)
    
    elif num == 4:
        plt.clf()

        x = ['No Events']
        y = [0]
        for events in df['Events']:
            if events == ' ':
                y[0] += 1
                continue

            event_list = list(events.split(' , '))
            for event in event_list:
                if event in x:
                    event_index = x.index(event)
                    y[event_index] += 1
                else:
                    x.append(event)
                    y.append(1)
        
        plt.figure(figsize=(10, 5))
        plt.bar(x, y)
        plt.grid()
        plt.title('Event Counts')
        plt.xlabel('Events')
        plt.ylabel('Count')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
        buffer.close()

        replies = Reply.objects.all()
        context = {
            'problem_num': 4,
            'chart_image': f'data:image/png;base64,{image_base64}',
            'replies': replies,
        }

        return render(request, 'problem4.html', context)


def create(request, num):
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save()
            return redirect('weathers:problem', num=reply.problem_num)
    else:
        form = ReplyForm()

    context = {
        'num': num,
        'form': form,
    }
    return render(request, 'create.html', context)


def delete(request, pk, num):
    reply = Reply.objects.get(pk=pk)
    reply.delete()
    return redirect('weathers:problem', num=num)


def update(request, pk, num):
    reply = Reply.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            form.save()
            return redirect('weathers:problem', num=num)
    else:
        form = ReplyForm(instance=reply)
    context = {
        'reply': reply,
        'form': form,
        'num': num,
        'pk': pk,
    }
    return render(request, 'update.html', context)