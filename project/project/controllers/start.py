from django.shortcuts import render
from project.models import (
    Type_Place,
    Place,
    Image_Place,
    Type_Service,
    Service,
    Service_Place,
    Line_Day,
    Schedule_Service,
    Rol,
)
from django.conf import settings

def run(request):
    response = {}
    request.session['user'] = {
        'id': 0,
        'name': 'Desarrollador',
        'email': 'josecheche14@gmail.com',
    }
    response['session'] = request.session['user']

    roles = [
        {
            'name': 'Administrador',
            'description': 'Crea y asigna a los encargados a cada sitio de interes.',
        },
        {
            'name': 'Encargado',
            'description': 'Administra los servicios del sitio de interes asignado.',
        },
        {
            'name': 'Usuario',
            'description': 'Puede navegar, ver los sitios de interes y utilizar los servicios.',
        },
    ]

    for rol in roles:
        try:
            rol_val = Rol.objects.get(name=rol['name'])
            rol_val.description = rol['description']
            rol_val.save()
        except Rol.DoesNotExist:
            rol_val = Rol()
            rol_val.name = rol['name']
            rol_val.description = rol['description']
            rol_val.save()


    type_places = [
        {
            'name': 'Servicio',
            'description': 'Dónde el usuario pedirá alguna prestación de la Universidad, ya sea: Una reserva o un pedido.',
        },
        {
            'name': 'Informativo',
            'description': 'Dónde el usuario podrá saber horarios de atención de ciertos lugares.',
        },
    ]

    for type_place in type_places:
        try:
            type_place_val = Type_Place.objects.get(name=type_place['name'])
            type_place_val.description = type_place['description']
            type_place_val.save()
        except Type_Place.DoesNotExist:
            type_place_val = Type_Place()
            type_place_val.name = type_place['name']
            type_place_val.description = type_place['description']
            type_place_val.save()

    type_services = [
        {
            'name': 'Ventas',
            'description': 'Servicios orientados a la venta de productos.',
        },
        {
            'name': 'Reserva',
            'description': 'Servicios para el uso de los estudiantes con previa reserva y por tiempo limitado.',
        },
        {
            'name': 'Uso',
            'description': 'Servicios para el uso en general.',
        },
    ]

    for type_service in type_services:
        try:
            type_service_val = Type_Service.objects.get(name=type_service['name'])
            type_service_val.description = type_service['description']
            type_service_val.save()
        except Type_Service.DoesNotExist:
            type_service_val = Type_Service()
            type_service_val.name = type_service['name']
            type_service_val.description = type_service['description']
            type_service_val.save()

    places = [
        {
            'name': 'Restaurante',
            'description': 'La sección de la Universidad Manuela Beltrán donde los estudiantes pueden ordenar comida y bebidas. Aquí puedes ordenar comida para que solo pases por ella a pagar.',
            'type': 'Informativo',
            'image': [
                'restaurante_1.jpg'
            ],
            'service': [
                {
                    'name': 'Almuerzos',
                    'description': 'Ordenar el tipo de almuerzo que se desee. Hay varios tipos de almuerzos disponibles.',
                    'type': 'Ventas',
                    'line_day': [
                        {
                            'day': 1,
                            'start': '10:00',
                            'end': '20:00',
                        },
                    ] 
                },
            ]
        },
        {
            'name': 'Pasillo',
            'description': 'La sección de la Universidad Manuela Beltrán donde se guardan las pertenencias de los estudiantes. Aquí puedes reservar un casillero para guardar tus pertenencias.',
            'type': 'Servicio',
            'image': [
                'casillero_1.jpg'
            ],
            'service': [
                {
                    'name': 'Casillero',
                    'description': 'Reservar casillero para guardar pertenencias.',
                    'type': 'Reserva',
                    'line_day': []
                },
            ]
        },
        {
            'name': 'Baño',
            'description': 'Aquí puedes saber los horarios de disponibilidad de los baños.',
            'type': 'Informativo',
            'image': [
                'baño_1.jpg'
            ],
            'service': [
                {
                    'name': 'Servicio al baño',
                    'description': 'Disponibilidad del servicio al baño.',
                    'type': 'Uso',
                    'line_day': []
                },
            ]
        },
        {
            'name': 'Cafeteria',
            'description': 'La sección de la Universidad Manuela Beltrán donde los estudiantes pueden ordenar aperitivos. Aquí puedes ordenar el aperitivo que quieras, para que solo pases al 4to piso a pagar y reclamarlo.',
            'type': 'Servicio',
            'image': [
                'cafeteria_1.jpg'
            ],
            'service': [
                {
                    'name': 'Pizzeria',
                    'description': 'Ordenar porción de pizza para que esté lista cuando se pase a recoger.',
                    'type': 'Ventas',
                    'line_day': []
                },
                {
                    'name': 'Nativos',
                    'description': 'Ordenar bebida para que esté lista cuando pase a recoger.',
                    'type': 'Ventas',
                    'line_day': []
                },
            ]
        },
        {
            'name': 'Biblioteca',
            'description': 'Sección de la Universidad Manuela Beltrán donde los estudiantes pueden reservar computadores. Aquí puedes revervar computadores para que solo entres y lo puedas usar.',
            'type': 'Servicio',
            'image': [
                'biblioteca_1.jpg'
            ],
            'service': [
                {
                    'name': 'Computadores',
                    'description': 'Reservar computador sin necesidad de apartarlo presencialmente.',
                    'type': 'Reserva',
                    'line_day': []
                },
            ]
        },
    ]

    for place in places:
        try:
            type_val = Type_Place.objects.get(name=place['type'])
            try:
                place_val = Place.objects.get(name=place['name'])
                place_val.description = place['description']
                place_val.type_place = type_val
                place_val.save()
            except Place.DoesNotExist:
                place_val = Place()
                place_val.name = place['name']
                place_val.description = place['description']
                place_val.type_place = type_val
                place_val.save()

            location = 1
            for image in place['image']:
                path_image = 'images/sites/' + image
                try:
                    image_val = Image_Place.objects.get(place=place_val, image=path_image)
                    image_val.location = location
                    image_val.save()
                except Image_Place.DoesNotExist:
                    image_val = Image_Place()
                    image_val.place = place_val
                    image_val.image = path_image
                    image_val.location = location
                    image_val.save()
                location += 1

            for service in place['service']:
                try:
                    type_service_val = Type_Service.objects.get(name=service['type'])
                    try:
                        service_val = Service.objects.get(name=service['name'])
                        service_val.description = service['description']
                        service_val.type_service = type_service_val
                        service_val.save()
                    except Service.DoesNotExist:
                        service_val = Service()
                        service_val.name = service['name']
                        service_val.description = service['description']
                        service_val.type_service = type_service_val
                        service_val.save()
                    # Relación Servicio y Sitio de Interes
                    try:
                        service_place_val = Service_Place.objects.get(place=place_val, service=service_val)
                        service_place_val.state = True
                        service_place_val.save()
                    except Service_Place.DoesNotExist:
                        service_place_val = Service_Place()
                        service_place_val.place = place_val
                        service_place_val.service = service_val
                        service_place_val.save()

                    # Horario
                    for line_day in service['line_day']:
                        try:
                            line_day_val = Line_Day.objects.get(day=line_day['day'])
                            line_day_val.start_hour = line_day['start']
                            line_day_val.end_hour = line_day['end']
                            line_day_val.save()
                        except Line_Day.DoesNotExist:
                            line_day_val = Line_Day()
                            line_day_val.day = line_day['day']
                            line_day_val.start_hour = line_day['start']
                            line_day_val.end_hour = line_day['end']
                            line_day_val.save()
                        # Relación Horario y el Servicio
                        try:
                            schedule_service_val = Schedule_Service.objects.get(service=service_val, line_day=line_day_val)
                            schedule_service_val.state = True
                            schedule_service_val.save()
                        except Schedule_Service.DoesNotExist:
                            schedule_service_val = Schedule_Service()
                            schedule_service_val.service = service_val
                            schedule_service_val.line_day = line_day_val
                            schedule_service_val.save()
                except Type_Service.DoesNotExist:
                    pass
        except Type_Place.DoesNotExist:
            pass

    response['data'] = places

    return render(request, 'start/run.html', context=response)