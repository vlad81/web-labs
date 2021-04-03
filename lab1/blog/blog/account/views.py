import json

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import JsonResponse


def register(request):
    if request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']
        email = request.GET['email']
        user = User.objects.create(username=username, password=password, email=email)
        user.save()
        data = {
            'successful_register': True
        }
        return JsonResponse(data, safe=False)

    data = {
        'successful_register': False
    }
    return JsonResponse(data, safe=False)


def login_page(request):
    if request.method == 'GET':
        email = request.GET['email']
        password = request.GET['password']
        user_obj = User.objects.get(email=email)
        if user_obj is not None:
            user = authenticate(username=user_obj.username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    data = {
                        'successful_login': True,
                        'username': user_obj.username
                    }
                    return JsonResponse(data, safe=False)

    data = {
        'successful_login': False
    }

    return JsonResponse(data, safe=False)


@staff_member_required
def del_user(request):
    try:
        u = User.objects.get(username=request.GET['username'])
        u.delete()
        data = {
            'successful_delete': True
        }

        return JsonResponse(data, safe=False)

    except Exception as e:
        data = {
            'successful_delete': False
        }

        return JsonResponse(data, safe=False)


def home(request):
    current_user = request.user
    if current_user.is_authenticated:
        username = current_user.username
        email = current_user.email

        data = {
            "username": username,
            "email": email,
            "date_joined": json.dumps(current_user.date_joined, cls=DjangoJSONEncoder)
        }
    else:
        data = {
            'error': "Non-logged user."
        }

    return JsonResponse(data, safe=False)
