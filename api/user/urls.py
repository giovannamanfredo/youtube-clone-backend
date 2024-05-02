from django.urls import path
from .views import CreatorList, CreatorDetail

urlpatterns = [
    path('creator', CreatorList.as_view(), name='creator-list'),
    path('creator/<str:username>', CreatorDetail.as_view(), name='creator-detail'),
]