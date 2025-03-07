from django.urls import path, include
from .views import HomeListView, CreateRoomCreateView, RoomDetailView, ProfileUpdateView
from rest_framework.routers import DefaultRouter
from .api_views import UserViewSet, RoomViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', HomeListView.as_view(), name='home'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('room/create/', CreateRoomCreateView.as_view(), name='create_room'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room'),
]
