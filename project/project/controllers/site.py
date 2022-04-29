from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
from project.encrypt import Encrypt
from project.models import User_College, User_Place

@never_cache
def login(request, code=None):
    response = {}
    if request.method == "POST":
        data = request.POST
        if 'password' in data and 'email' in data:
            if data['email'] != '' and data['password'] != '':
                password = data['password']
                email = data['email']
                try:
                    user_val = User_College.objects.get(email=email)
                    response['status'] = 'success'
                    response['message'] = 'Login exitoso'
                    if Encrypt().verify(password, user_val.password):
                        request.session['user'] = {
                            'id': user_val.id,
                            'name': user_val.name,
                            'email': user_val.email,
                            'rol': user_val.rol_id,
                            'rol_name': user_val.rol.name,
                        }
                        response['session'] = request.session['user']
                        return HttpResponseRedirect('/index/')
                    else:
                        response['status'] = 'fail'
                        response['message'] = 'Clave incorrecta'
                except User_College.DoesNotExist:
                    response['status'] = 'fail'
                    response['message'] = 'El usuario no existe'  
    elif code == 1:
        response['status'] = 'success'
        response['message'] = 'El usuario fue registrado con exito'
        return render(request, 'site/login.html', context=response)
                    
    return render(request, 'site/login.html', context=response)

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return HttpResponseRedirect('/login/')

@never_cache
def signup(request):
    response = {}
    if request.method == "POST":
        data = request.POST
        print(data['name'])

        if 'name' in data and 'identification' in data and 'phone' in data and 'email' in data and 'password' in data:
            if data['name'] != '' and data['identification'] != '' and data['phone'] != '' and data['email'] != '' and data['password'] != '':
                name = data['name']
                identification = data['identification']
                phone = data['phone']
                email = data['email']
                password = data['password']

                if not User_College.objects.filter(email=email):
                    password_encrypt = Encrypt().encrypt_code(password)
                    new_user = User_College()
                    new_user.name = name
                    new_user.identification = identification
                    new_user.email = email
                    new_user.phone = phone
                    new_user.rol_id = 3
                    new_user.password = password_encrypt
                    new_user.save()
                    response['status'] = 'success'
                    
                    # recipient_list = [new_user.email,]
                    # Email().welcome(recipient_list)

                    return HttpResponseRedirect('/login/1/')
                else:
                    response['status'] = 'fail'
                    response['message'] = 'El usuario ya existe'

    return render(request, 'site/signup.html', context=response)

def index(request):
    if 'user' in request.session:
        if request.method == "POST":
            print('POST ----')
        return render(request, 'site/index.html', context={'session': request.session['user']})
    else:
        return HttpResponseRedirect('/login/')

def plans(request):
    if 'user' in request.session:
        return render(request, 'site/plans.html', context={'session': request.session['user']})
    else:
        return HttpResponseRedirect('/login/')

def manage(request):
    if 'user' in request.session:
        if request.session['user']['rol'] == 1:
            response = {}
            if request.method == "POST":
                data = request.POST
                print(data['name'])

                if 'name' in data and 'identification' in data and 'phone' in data and 'email' in data and 'password' in data and 'place' in data:
                    if data['name'] != '' and data['identification'] != '' and data['phone'] != '' and data['email'] != '' and data['password'] != '' and data['place'] != '':
                        name = data['name']
                        identification = data['identification']
                        phone = data['phone']
                        email = data['email']
                        password = data['password']
                        place = data['place']
                        password_encrypt = Encrypt().encrypt_code(password)

                        print('data:::::::::::::::::::')
                        print(data)

                        if User_College.objects.filter(email=email) and data['id'] == '':
                            response['status'] = 'fail'
                            response['message'] = 'El usuario ya existe'
                        else:
                            manage_process = True
                            if data['id'] != '':
                                try:
                                    manage_val = User_College.objects.get(id=data['id'])
                                    manage_val.name = name
                                    manage_val.identification = identification
                                    manage_val.email = email
                                    manage_val.phone = phone
                                    if password != manage_val.password:
                                        manage_val.password = password_encrypt
                                    manage_val.save()
                                except User_College.DoesNotExist:
                                    manage_process = False
                                    response['status'] = 'fail'
                                    response['message'] = 'El usuario no existe'
                            else:
                                manage_val = User_College()
                                manage_val.name = name
                                manage_val.identification = identification
                                manage_val.email = email
                                manage_val.phone = phone
                                manage_val.rol_id = 2
                                manage_val.password = password_encrypt
                                manage_val.save()
                                response['status'] = 'success'

                            if manage_process:
                                try:
                                    user_place_val = User_Place.objects.get(user_college=manage_val)
                                    user_place_val.place_id = place
                                    user_place_val.state = True
                                    user_place_val.save()
                                except User_Place.DoesNotExist:
                                    user_place_val = User_Place()
                                    user_place_val.user_college = manage_val
                                    user_place_val.place_id = place
                                    user_place_val.save()

                            return HttpResponseRedirect('/manage/')


            manage_list = User_College.objects.filter(
                rol_id=2
            ).select_related(
                'user_place'
            ).values(
                'id',
                'name',
                'identification',
                'email',
                'phone',
                'password',
                'user_place__place_id',
                'user_place__place__name',
            )
            response['session'] = request.session['user']
            response['managers'] = manage_list
            return render(request, 'site/manage.html', context=response)
    return HttpResponseRedirect('/logout/')
