from django.urls import include, path
from .import views
from .import api

urlpatterns = [
    path('api/protein/<int:pk>', api.ProteinDetails.as_view()),
]