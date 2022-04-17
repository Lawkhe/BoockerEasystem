from django.shortcuts import render, redirect
from django.http import JsonResponse
from project.models import (
    Place,
    Image_Place,
    Service_Place,
    Schedule_Service,
)

def detail(request, pk):
    response = {}
    # request.session['user'] = {
    #     'id': 0,
    #     'name': 'Desarrollador',
    #     'email': 'josecheche14@gmail.com',
    # }
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
                    # 'start': schedule_service_val.line_day.start_hour,
                    # 'end': schedule_service_val.line_day.end_hour,
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

def get_data(request, pk):
    data_place = {}
    try:
        place_val = Place.objects.get(id=pk)
        image = ''
        image_val = Image_Place.objects.filter(place=place_val)
        if image_val:
            image = str(image_val[0].image)

        data_place = {
            'id': place_val.id,
            'name': place_val.name,
            'description': place_val.description,
            'type': place_val.type_place.name,
            'image': image
        }
    except Place.DoesNotExist:
        pass
    return JsonResponse(data_place)