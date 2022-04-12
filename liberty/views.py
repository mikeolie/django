from django.http import HttpResponse, JsonResponse
from django_auth_ldap.backend import LDAPBackend


def index(request):
    return HttpResponse("Hello, world. You're at the Liberty index.")


def products(request):
    user = LDAPBackend().populate_user('molie')
    if user is None:
        raise Exception("No User found")
    return JsonResponse({'message': "Success"})
