from msilib.schema import Patch

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from TaskApp.models import *

from .serializers import *


class registration(APIView):
    def post(self,request):
        try:
            userobj=Profile.objects.get(email=request.data['email'],is_active=True)
        except exception as e:
            userobj=''
        if userobj=='':
            if request.data['email'] is None or request.data['password'] is None or request.data['name'] is None or request.data['phone_number'] is None:
                return Response({'error': 'Please name,email,phone no,password is required!!'},
                        status=HTTP_400_BAD_REQUEST)
            else:
                userobj=Profile()
                userobj.first_name=request.data['name']
                userobj.email=request.data['email']
                userobj.username=request.data['email']
                userobj.phone_number=request.data['phone_number']
                userobj.name=request.data['name']
                userobj.date_of_birth=request.data['date_of_birth']
                userobj.set_password(request.data['password'])
                userobj.save()
                return Response({'message':'user registration successfully!!!'},status=HTTP_201_CREATED)

class registration_list(APIView):
    def get(self,request):
        userlist=Profile.objects.filter(is_active=True)
        serializerobj=registrationserializer(userlist,many=True)
        return JsonResponse(serializerobj.data,safe=False)
        
class profile_details(APIView):
    def get(self,request):
        userlist=Profile.objects.filter(email=request.user.email,is_active=True)
        serializerobj=registrationserializer(userlist,many=True)
        return JsonResponse(serializerobj.data,safe=False)

class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response({'message':'user logout successfully'},status=status.HTTP_200_OK)

class profile_update(APIView):
    def post(self, request):
        serializer = registrationserializer(request.user, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            #serializer.first_name=request.data['name']
            serializer.save()
            return JsonResponse(status=status.HTTP_200_OK, data=serializer.data,safe=False)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data="wrong parameters",safe=False)

class profiledata_filter(APIView):
    def get(self,request):
        userobj=Profile.objects.filter(is_active=True)
        if request.data['gender'] is not None and request.data['gender'] is not '':
            userobj=userobj.filter(gender=request.data['gender'])
        if request.data['permanent_address_city'] is not None and request.data['permanent_address_city'] is not '':
            userobj=userobj.filter(permanent_address__city=request.data['permanent_address_city'])
        serializerobj=registrationserializer(userobj,many=True)
        return JsonResponse(serializerobj.data,safe=False)
