from django.urls import include, path
from .import views
from .import api

urlpatterns = [
    path('', views.index, name='index'),
    path('api/protein/<protein_id>', api.ProteinDetails.as_view(), name='protein_api'),
    path('api/pfam/<domain_id>', api.PfamDetails.as_view(), name='pfam_api'),
    path('api/proteins/<taxa_id>', api.ProteinList.as_view(), name='proteins_api'),
    path('api/pfams/<taxa_id>', api.PfamList.as_view(), name='pfams_api'),
    path('api/coverage/<protein_id>', api.CoverageDetails.as_view(), name='coverage_api')
]