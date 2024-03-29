import json
import environ
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from django.contrib.auth import logout, login
from django_auth_ldap.backend import LDAPBackend

from liberty.models import Category, Products, RequestLog

env = environ.Env()
auth = LDAPBackend()


def index(request):
    if request.user.is_authenticated:
        return JsonResponse({"message": "authenticated"})
    return HttpResponse("Hello, world. You're at the Liberty index.")


def signIn(request):
    user = auth.authenticate(request, username=env(
        'MY_LDAP_USER'), password=env('MY_LDAP_PASS'))
    if user is None:
        return JsonResponse({"message": "Unauthorized"}, status=401)

    login(request, user=user, backend='django.contrib.auth.backends.ModelBackend')
    return JsonResponse({'message': "Signed In!"})


def signOut(request):
    logout(request)
    return JsonResponse({"message": "Signed Out!"})


@csrf_exempt
def products(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        try:
            category_id = json_data["categories"]
            json_data["categories"] = Category.objects.get(id=category_id)
            new_product = Products.objects.create(**json_data)
            message = {
                "message": f"New product created with id: {new_product.id}"
            }
            return JsonResponse(message)
        except KeyError:
            return HttpResponseServerError("Malformed Data")
    queryset = Products.objects.all().values()
    data_list = list(queryset)
    return JsonResponse({"data": data_list})


def requestlog(request):
    queryset = RequestLog.objects.all().values()
    data_list = list(queryset)
    return JsonResponse({"data": data_list})
