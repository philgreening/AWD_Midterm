from rest_framework import generics
from rest_framework import mixins

from .models import *
from. serializers import *

#  looks up protein id and returns protein details in JSON format
class ProteinDetails(mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):

    queryset = Protein.objects.all()
    lookup_field = 'protein_id'
    serializer_class = ProteinSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

#  looks up domain id and returns pfam details in JSON format
class PfamDetails(mixins.RetrieveModelMixin,
                  generics.GenericAPIView):

    queryset = PfamDescriptions.objects.all()
    lookup_field = 'domain_id'
    serializer_class = PfamSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  

#  looks up taxa id and returns a list of matching proteins JSON format
class ProteinList(mixins.RetrieveModelMixin,
                  generics.ListAPIView):
                  
    lookup_field = 'taxa_id'
    serializer_class = ProteinListSerializer

    def get_queryset(self):
        taxa_id = self.kwargs['taxa_id']
        return Protein.objects.filter(taxa_id = taxa_id)

#  looks up taxa id and returns a list of matching domains JSON format
class PfamList(mixins.RetrieveModelMixin,
                  generics.ListAPIView):

    lookup_field = 'taxa_id'
    serializer_class = PfamListSerializer

    def get_queryset(self):
        taxa_id = self.kwargs['taxa_id']
        return Domain.objects.filter(taxa_id__taxa_id = taxa_id)

#  looks up protein id and returns the coverage in JSON format
class CoverageDetails(mixins.RetrieveModelMixin,
                      generics.ListAPIView):
    lookup_field = 'protein_id'

    serializer_class = CoverageSerializer

    def get_queryset(self):
        protein_id = self.kwargs['protein_id']
        return Domain.objects.filter(protein_id__protein_id = protein_id)


    







