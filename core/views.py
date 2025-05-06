from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt


def index(request):
    if request.method == 'POST':
        texto = request.POST['texto']
        start = request.POST['start']
        return JsonResponse({'key':start, 'texto': texto})
    if request.method == 'GET':
        return render(request, 'index.html')