from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from project.models import (
    Image_Place,
    Line_Day,
    Place,
    Service,
    Service_Place,
    Schedule_Service,
    User_Place,
)


def place(request):
    if 'user' in request.session:
        if request.session['user']['rol'] == 2:
            response = {}
            response['session'] = request.session['user']

            try:
                if request.method == "POST":
                    data = request.POST
                    print('data:::::::::::::::::')
                    print(data)
                    line_day_val = Line_Day()
                    line_day_val.day = data['day']
                    line_day_val.start_hour = data['start']
                    line_day_val.end_hour = data['end']
                    line_day_val.save()
                    # Relación Horario y el Servicio
                    if data['id'] != '':
                        schedule_service_val = Schedule_Service.objects.get(id=data['id'], service_id=data['service'])
                        schedule_service_val.line_day = line_day_val
                        schedule_service_val.state = True
                        schedule_service_val.save()
                    else:
                        schedule_service_val = Schedule_Service()
                        schedule_service_val.line_day = line_day_val
                        schedule_service_val.service_id = data['service']
                        schedule_service_val.save()

                    return HttpResponseRedirect('/place/')

                user_place_val = User_Place.objects.get(user_college_id=request.session['user']['id'])
                place_val = Place.objects.get(id=user_place_val.place_id)

                services_data = []
                service_place_values = Service_Place.objects.filter(place=place_val)
                for service_place_val in service_place_values:

                    schedule_data = []
                    schedule_service_values = Schedule_Service.objects.filter(service_id=service_place_val.service_id, state=True)
                    for schedule_service_val in schedule_service_values:
                        day_array = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
                        schedule_data.append({
                            'id': schedule_service_val.line_day_id,
                            'day': schedule_service_val.line_day.day,
                            'day_name': day_array[schedule_service_val.line_day.day-1],
                            'start': schedule_service_val.line_day.start_hour,
                            'end': schedule_service_val.line_day.end_hour,
                        })
                    services_data.append({
                        'id': service_place_val.service_id,
                        'name': service_place_val.service.name,
                        'description': service_place_val.service.description,
                        'schedule': schedule_data,
                    })

                # print('services_data')
                # print(services_data)

                data_place = {
                    'name': place_val.name,
                    'description': place_val.description,
                    'type': place_val.type_place.name,
                    'services': services_data,
                }
                response['data'] = data_place

                return render(request, 'place/place.html', context=response)
            except User_Place.DoesNotExist:
                pass
            except Place.DoesNotExist:
                pass
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')

def detail(request, pk):
    if 'user' in request.session:
        response = {}
        response['session'] = request.session['user']
        
        try:
            place_val = Place.objects.get(id=pk)
            services_data = []
            service_place_values = Service_Place.objects.filter(place=place_val)
            for service_place_val in service_place_values:

                schedule_data = []
                schedule_service_values = Schedule_Service.objects.filter(service_id=service_place_val.service_id)
                for schedule_service_val in schedule_service_values:
                    schedule_data.append({
                        'day': schedule_service_val.line_day.day,
                        'start': schedule_service_val.line_day.start_hour,
                        'end': schedule_service_val.line_day.end_hour,
                    })
                services_data.append({
                    'id': service_place_val.service_id,
                    'name': service_place_val.service.name,
                    'description': service_place_val.service.description,
                    'schedule': schedule_data,
                })

            print('services_data')
            print(services_data)

            data_place = {
                'name': place_val.name,
                'description': place_val.description,
                'type': place_val.type_place.name,
                'services': services_data,
            }
            response['data'] = data_place
        except Place.DoesNotExist:
            return redirect('/plans/')
        return render(request, 'place/detail.html', context=response)
    else:
        return HttpResponseRedirect('/login/')

def get_data(request, pk):
    data_place = {}
    try:
        place_val = Place.objects.get(id=pk)
        image = ''
        image_val = Image_Place.objects.filter(place=place_val)
        if image_val:
            image = str(image_val[0].image)


        services_data = []
        service_place_values = Service_Place.objects.filter(place=place_val)
        for service_place_val in service_place_values:

            schedule_data = []
            schedule_service_values = Schedule_Service.objects.filter(service_id=service_place_val.service_id)
            for schedule_service_val in schedule_service_values:
                schedule_data.append({
                    'day': schedule_service_val.line_day.day,
                    'start': schedule_service_val.line_day.start_hour,
                    'end': schedule_service_val.line_day.end_hour,
                })
            services_data.append({
                'id': service_place_val.service_id,
                'name': service_place_val.service.name,
                'description': service_place_val.service.description,
                'schedule': schedule_data,
            })

        data_place = {
            'id': place_val.id,
            'name': place_val.name,
            'description': place_val.description,
            'type': place_val.type_place.name,
            'image': image,
            'services': services_data,
        }
    except Place.DoesNotExist:
        pass
    return JsonResponse(data_place)

def service(request, pk):
    if 'user' in request.session:
        response = {}
        response['session'] = request.session['user']
        
        try:
            service_val = Service.objects.get(id=pk)
            data_service = {
                'name': service_val.name,
                'description': service_val.description,
            }
            response['data'] = data_service
            return render(request, 'place/service.html', context=response)
        except Service.DoesNotExist:
            pass
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')