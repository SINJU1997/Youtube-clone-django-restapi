from django.contrib import admin
from django.urls import path
from . import views
from . views import Youtubecvlview
urlpatterns = [
    path('youtube',Youtubecvlview.as_view())
]
