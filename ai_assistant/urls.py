from django.urls import path

from .views import (
    DatasetUploadView,
    DatasetQueryView, DatasetListView
)
from .views import chat_page
urlpatterns = [

    path('upload-dataset/',DatasetUploadView.as_view(),name='upload-dataset'),
    path('query-dataset/',DatasetQueryView.as_view(),name='query-dataset'),
    path('chat/',chat_page,name='chat-page'),
    path("datasets/",DatasetListView.as_view(),name="datasets"),
]