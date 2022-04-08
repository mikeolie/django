from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Liberty index.")


def products(request):
    return JsonResponse({'message': "Success"})
