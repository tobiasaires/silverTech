from django.urls import path, include
from rest_framework import routers
from .views import (UserView, MemoryView, MotherBoardView,
                    VideoBoardView, ProcessorView, ComputerView)

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'processors', ProcessorView)
router.register(r'memories', MemoryView)
router.register(r'mother-boards', MotherBoardView)
router.register(r'video-boards', VideoBoardView)
router.register(r'computers', ComputerView)


urlpatterns = [
    path('api/', include(router.urls)),
]
