from django.urls import include, path
from .import views
from .import api

urlpatterns = [
    path('api/protein/<protein_id>', api.ProteinDetails.as_view(), name='protein_api'),
    path('api/sequence/<int:pk>', api.SequencingDetails.as_view(), name='sequence_api'),
    path('api/pfam/<int:pk>', api.PfamDetails.as_view(), name='pfam_api'),
]