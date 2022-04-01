from django.shortcuts import render

def detail(request, pk):
    response = {}
    request.session['user'] = {
        'id': 0,
        'name': 'Desarrollador',
        'email': 'josecheche14@gmail.com',
    }
    response['session'] = request.session['user']
    return render(request, 'place/detail.html', context=response)