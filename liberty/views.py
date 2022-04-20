from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
import json
from venv import create
import environ
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django_auth_ldap.backend import LDAPBackend
from django.contrib.auth import logout, login

from liberty.models import Products, RequestLog

from liberty.serializers import RequestlogSerializer, CreateRequestLogSerializer

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
    queryset = Products.objects.all().values()
    data_list = list(queryset)
    return JsonResponse({"data": data_list})


def requestlog(request):
    if request.method == "POST":
        return JsonResponse({"data": "Hello Post"})
    queryset = RequestLog.objects.all().values()
    data_list = list(queryset)
    return JsonResponse({"data": data_list})


class RequestLogView(generics.ListAPIView):
    queryset = RequestLog.objects.all()
    serializer_class = RequestlogSerializer


class CreateRequestLogView(APIView):
    serializer_class = CreateRequestLogSerializer

    def post(self, request, format=None):
        pass

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            advisor = serializer.data.get('advisor')
            customer = serializer.data.get('customer')
            description = serializer.data.get('description')
            budget = serializer.data.get('budget')
            grade = serializer.data.get('grade')
            notes = serializer.data.get('notes')
            host =  # need to connect it to a host, I suppose LDAP
            queryset = RequestLog.objects.filter(host=host)
            if queryset.exists():
                print('n/a')
            else:
                create = RequestLog(host=host, advisor=advisor, customer=customer,
                                    description=description, budget=budget, grade=grade, notes=notes,)
                create.save()

            return Response(RequestlogSerializer(create).data, status=status.HTTP_200_OK)
