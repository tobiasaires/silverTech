from django.contrib import admin
from .models import (Processor, Memory, MotherBoard, VideoBoard, Computer)
# Register your models here.

admin.site.register(Processor)
admin.site.register(Memory)
admin.site.register(MotherBoard)
admin.site.register(VideoBoard)
admin.site.register(Computer)
