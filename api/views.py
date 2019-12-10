from rest_framework import viewsets
from .models import (User, Processor, MotherBoard, VideoBoard, Memory)
from .serializers import *


class UserView(viewsets.ReadOnlyModelViewSet):
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
