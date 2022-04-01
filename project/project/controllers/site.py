from django.shortcuts import render
from django.views.decorators.cache import never_cache

@never_cache
def login(request):
    response = {}
    return render(request, 'site/login.html', context=response)

def index(request):
    response = {}
    request.session['user'] = {
        'id': 0,
        'name': 'Desarrollador',
        'email': 'josecheche14@gmail.com',
    }
    response['session'] = request.session['user']
    return render(request, 'site/index.html', context=response)

def plans(request):
    response = {}
    request.session['user'] = {
        'id': 0,
        'name': 'Desarrollador',
        'email': 'josecheche14@gmail.com',
    }
    response['session'] = request.session['user']
    return render(request, 'site/plans.html', context=response)