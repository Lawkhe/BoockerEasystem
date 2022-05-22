from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from project.models import (
    Catalog_Service,
    Service,
    Order_Service,
    Order_Catalog,
    Schedule_Service,
    Traceability_Order_Service,
)
from rest_framework.decorators import api_view
# from datetime import date, time

from datetime import datetime
import pusher
import json

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

@api_view(['POST'])
def add_service(request):
    data_request = {
        'status': 'error'
    }
    if 'user' in request.session:
        if request.method == "POST":
            data = request.POST

            service_id = 0
            limit = False
            today_now = datetime.now()
            for catalog in json.loads(data['catalog']):
                if service_id == 0:
                    service_id = Catalog_Service.objects.get(id=catalog['id']).service_id
                    try:
                        day_num = today_now.weekday() + 1
                        hour_now = "{:d}:{:02d}:00".format(today_now.hour, today_now.minute)
                        date_time_obj = datetime.strptime(hour_now, '%H:%M:%S')
                        schedule_service_val = Schedule_Service.objects.get(
                            service_id=service_id,
                            line_day__day=day_num,
                            state=True
                        )
                        if not (date_time_obj.time() > schedule_service_val.line_day.start_hour and date_time_obj.time() < schedule_service_val.line_day.end_hour):
                            limit = True
                    except Schedule_Service.DoesNotExist:
                        limit = True

            if not limit:

                order_val = Order_Service()
                order_val.user_college_id = request.session['user']['id']
                order_val.status = 1 
                order_val.save()

                for catalog in json.loads(data['catalog']):
                    order_service_val = Order_Catalog()
                    order_service_val.order_service = order_val
                    order_service_val.catalog_service_id = catalog['id']
                    order_service_val.quantity = catalog['num']
                    order_service_val.save()
                
                traceability_order_val = Traceability_Order_Service()
                traceability_order_val.order_service = order_val
                traceability_order_val.action = 'Creado'
                traceability_order_val.description = 'Servicio realizado'
                traceability_order_val.save()

                pusher_client = pusher.Pusher(
                    app_id='1411834',
                    key='05321c7f890e35ee486b',
                    secret='de01362e0ab27e26478c',
                    cluster='us2',
                    ssl=True
                )

                order_data = {
                    'id': order_val.id,
                    'name': order_val.user_college.name,
                    'date': str(order_val.date)
                }

                pusher_client.trigger('my-channel-' + str(service_id), 'my-event', {
                    'title': 'Confirmar',
                    'message': 'Nuevo pedido agregado',
                    'order': order_data
                })

                data_request['status'] = 'success'

    return JsonResponse(data_request)

def get_order(request, pk):
    data_order = {}
    try:
        order_service_val = Order_Service.objects.get(id=pk)
        catalog_data = []
        total = 0
        order_catalog_values = Order_Catalog.objects.filter(order_service_id=pk)
        for order_catalog_val in order_catalog_values:
            catalog_data.append({
                'name': order_catalog_val.catalog_service.name,
                'quantity': order_catalog_val.quantity,
                'total': order_catalog_val.catalog_service.cost * order_catalog_val.quantity,
            })
            total += order_catalog_val.catalog_service.cost * order_catalog_val.quantity

        data_order = {
            'id': order_service_val.id,
            'date': str(order_service_val.date),
            'status': order_service_val.status,
            'catalogs': catalog_data,
            'total': total,
        }
    except Order_Service.DoesNotExist:
        pass
    return JsonResponse(data_order)

def change_state(request, pk, status):
    response = {
        'status': 'error'
    }
    try:
        order_service_val = Order_Service.objects.get(id=pk)
        order_service_val.status = status
        order_service_val.save()

        pusher_client = pusher.Pusher(
            app_id='1411834',
            key='05321c7f890e35ee486b',
            secret='de01362e0ab27e26478c',
            cluster='us2',
            ssl=True
        )
        message = ''
        state = 'success'
        if status == 2:
            message = 'Tu servicio fue aceptado'
        elif status == 3:
            message = 'Tu servicio fue rechazado'
            state = 'warning'
        elif status == 4:
            message = 'Tu servicio ya esta listo'
        elif status == 5:
            message = 'El servicio fue entregado'
        pusher_client.trigger('my-channel-' + str(order_service_val.user_college_id), 'my-event', {
            'title': 'Servicio',
            'message': message,
            'state': state,
        })
        
        traceability_order_val = Traceability_Order_Service()
        traceability_order_val.order_service = order_service_val
        traceability_order_val.action = 'Modificado'
        traceability_order_val.description = message
        traceability_order_val.save()

        response['status'] = 'success'
    except Order_Service.DoesNotExist:
        pass
    return JsonResponse(response)