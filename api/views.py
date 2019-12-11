from rest_framework import viewsets, filters, generics
from .models import (User, Processor, MotherBoard,
                     VideoBoard, Memory, Computer, Order)
from .serializers import *


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = "__all__"


class ProcessorView(viewsets.ReadOnlyModelViewSet):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer
    filter_fields = "__all__"


class MotherBoardView(viewsets.ReadOnlyModelViewSet):
    queryset = MotherBoard.objects.all()
    serializer_class = MotherBoardSerializer
    filter_fields = "__all__"


class VideoBoardView(viewsets.ReadOnlyModelViewSet):
    queryset = VideoBoard.objects.all()
    serializer_class = VideoBoardSerializer
    filter_fields = "__all__"


class MemoryView(viewsets.ReadOnlyModelViewSet):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    filter_fields = "__all__"


class ComputerView(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    filter_fields = "__all__"


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fiedls = "__all__"
