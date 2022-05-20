from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from project.models import (
    Catalog_Service,
    Service,
)
import pusher

def request_service(request, pk):
    if 'user' in request.session:
        response = {}
        response['session'] = request.session['user']
        
        try:
            service_val = Service.objects.get(id=pk)
            catalog_values = Catalog_Service.objects.filter(service=service_val, state=True)

            data_service = {
                'name': service_val.name,
                'description': service_val.description,
                'catalogs': catalog_values,
            }
            response['data'] = data_service
            return render(request, 'service/request.html', context=response)
        except Service.DoesNotExist:
            pass
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')