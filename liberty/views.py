import environ
from django.http import HttpResponse, JsonResponse
from django_auth_ldap.backend import LDAPBackend

env = environ.Env()


def index(request):
    return HttpResponse("Hello, world. You're at the Liberty index.")

def signIn(request):
    return JsonResponse({ 'message': "Signed In!"})

def signOut(request):
    return JsonResponse({ "message": "Signed Out!"})

def products(request):
    auth = LDAPBackend()
    user = auth.authenticate(request, username=env('LDAP_USER'), password=env('LDAP_PASS'))
    if user is None:
        return JsonResponse({ "message": "unable to get user" })

    return JsonResponse({'message': "Success"})
