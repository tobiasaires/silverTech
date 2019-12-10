from rest_framework import viewsets
from .models import (User, Processor, MotherBoard, VideoBoard, Memory, Computer, Order)
from .serializers import *


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProcessorView(viewsets.ReadOnlyModelViewSet):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer


class MotherBoardView(viewsets.ReadOnlyModelViewSet):
    queryset = MotherBoard.objects.all()
    serializer_class = MotherBoardSerializer


class VideoBoardView(viewsets.ReadOnlyModelViewSet):
    queryset = VideoBoard.objects.all()
    serializer_class = VideoBoardSerializer


class MemoryView(viewsets.ReadOnlyModelViewSet):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer

class ComputerView(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer