from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer


# Create your views here.


# generics.ListCreateAPIView: 레코드를 표시하고 새 레코드를 만들기 위한 POST 호출 수락
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# generics.RetrieveUpdateAPIView: 레코드를 가져와서 표시하고 업데이트하기 위한 POST 호출을 수락하는 모든 기능 포함
# generics.DestroyAPIView: DELETE 호출을 수락하고 최종적으로 레코드를 삭제하는 모든 기능 포함
class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer