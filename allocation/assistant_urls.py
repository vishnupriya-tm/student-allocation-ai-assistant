from django.urls import path
from .assistant_views import AssistantAPIView

urlpatterns = [
    path(
        'assistant/',
        AssistantAPIView.as_view(),
        name='assistant'
    ),
]



