from django.shortcuts import render

def run(request):
    response = {}
    request.session['user'] = {
        'id': 0,
        'name': 'Desarrollador',
        'email': 'josecheche14@gmail.com',
    }
    response['session'] = request.session['user']

    place = {
        'name': '',
        'description': ''
    }

    response['data'] = place

    return render(request, 'start/run.html', context=response)