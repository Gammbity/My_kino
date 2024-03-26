from django.urls import include, path
from .views import *

urlpatterns = [
    path('aktyor/', AktyorApiView.as_view()),
    path('add-comment/', CommentApiView.as_view()),
    path('film/<int:pk>', AddAktyorViewSet.as_view({'post': 'add_aktyor'})),
]
