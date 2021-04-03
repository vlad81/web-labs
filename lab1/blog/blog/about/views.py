from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    data = {
        'app_name': 'JustBlog',
        'about': 'This is just blog created for study aims.'
    }

    return JsonResponse(data, safe=False)


def doc(request):
    return render(request, 'doc.html')
