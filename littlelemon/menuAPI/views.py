from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


@api_view()
def menu(request):
    return Response('This is the menu', status=status.HTTP_200_OK)