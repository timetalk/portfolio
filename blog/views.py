from django.shortcuts import render

def home_views(request, *args, **kwargs):
    return render(request, 'pages/home.html')
