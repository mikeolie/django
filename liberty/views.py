import environ
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django_auth_ldap.backend import LDAPBackend
from django.contrib.auth import logout, login

from liberty.models import Products

env = environ.Env()
auth = LDAPBackend()


def index(request):
    if request.user.is_authenticated:
        return JsonResponse({"message": "authenticated"})
    return HttpResponse("Hello, world. You're at the Liberty index.")


def signIn(request):
    user = auth.authenticate(request, username=env(
        'LDAP_USER'), password=env('LDAP_PASS'))
    if user is None:
        return JsonResponse({"message": "unable to get user"}, status=401)

    login(request, user=user, backend='django.contrib.auth.backends.ModelBackend')
    return JsonResponse({'message': "Signed In!"})


def signOut(request):
    logout(request)
    return JsonResponse({"message": "Signed Out!"})


def products(request):
    numismatic_coins = Products.objects.all()[:50]
    data = serializers.serialize('json', numismatic_coins)
    return JsonResponse({'message': "Success", "products": data})
