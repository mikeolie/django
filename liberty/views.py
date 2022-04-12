import environ
from django.http import HttpResponse, JsonResponse
from django_auth_ldap.backend import LDAPBackend

env = environ.Env()


def index(request):
    return HttpResponse("Hello, world. You're at the Liberty index.")


def products(request):
    auth = LDAPBackend()
    user = auth.authenticate(username='molie', password=env('MY_LDAP_PASS'))
    print(user)
    return JsonResponse({'message': "Success"})
