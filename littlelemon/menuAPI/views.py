from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view

from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer


@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)


@api_view()
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)


# generics.ListCreateAPIView: 레코드를 표시하고 새 레코드를 만들기 위한 POST 호출 수락
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# generics.RetrieveUpdateAPIView: 레코드를 가져와서 표시하고 업데이트하기 위한 POST 호출을 수락하는 모든 기능 포함
# generics.DestroyAPIView: DELETE 호출을 수락하고 최종적으로 레코드를 삭제하는 모든 기능 포함
class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer