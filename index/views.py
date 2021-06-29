from django.shortcuts import render

def IndexView(request):
    params = {
        'title': 'INDEX',
    }
    return render(request, 'index/index.html', params)