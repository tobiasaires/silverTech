from rest_framework import serializers
from .models import (Processor, Computer, Memory,
                     MotherBoard, VideoBoard, User, Computer)
from .validators import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class ProcessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Processor
        fields = "__all__"


class MotherBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = MotherBoard
        fields = "__all__"


class MemorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Memory
        fields = "__all__"


class VideoBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoBoard
        fields = "__all__"

class ComputerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Computer
        fields = "__all__"

    def validate(self, data):
        Validators.number_ram(data)
        Validators.ram_size(data)

        return data