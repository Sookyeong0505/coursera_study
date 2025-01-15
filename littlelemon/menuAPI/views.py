from tkinter import Menu

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# Create your views here.


@api_view(['GET', 'POST'])
def menu(request):
    return Response('This is the menu', status=status.HTTP_200_OK)


class MenuList(APIView):
    def get(self, request):
        return Response({'menus': 'This is the menu'}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({'menus': 'New menu is created'}, status=status.HTTP_201_CREATED)
