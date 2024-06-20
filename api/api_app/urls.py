from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path("all/", views.get_all, name="all")
]

urlpatterns = format_suffix_patterns(urlpatterns)