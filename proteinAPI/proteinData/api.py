from typing import Sequence
from django.db.models.query import QuerySet
from django.http import JsonResponse, HttpResponse, request
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

from .models import *
from. serializers import *

# @csrf_exempt

# def protein_detail(request, pk):
#     try:
#         protein = Protein.objects.get(pk=pk)
#     except Protein.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = ProteinSerializer(protein)
#         return JsonResponse(serializer.data)

# class ProteinList(generics.ListAPIView):
#     queryset = Protein.objects.all()
#     serializer_class = ProteinSerializer

class SequencingDetails(mixins.RetrieveModelMixin,
              generics.GenericAPIView):
    queryset = Sequencing.objects.all()
    serializer_class = SequencingSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class PfamDetails(mixins.RetrieveModelMixin,
              generics.GenericAPIView):
    queryset = PfamDescriptions.objects.all()
    lookup_field = 'domain_id'
    serializer_class = PfamSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)    

class ProteinDetails(mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = Protein.objects.all()
    lookup_field = 'protein_id'
    serializer_class = ProteinSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ProteinList(mixins.RetrieveModelMixin,
                  generics.ListAPIView):
    #queryset = Organism.objects.filter(taxa_id__exact = )
    lookup_field = 'taxa_id'
    serializer_class = ProteinListSerializer

    def get_queryset(self):
        taxa_id = self.kwargs['taxa_id']
        return Organism.objects.filter(taxa_id = taxa_id)

class PfamList(mixins.RetrieveModelMixin,
                  generics.ListAPIView):
    #queryset = Domain.objects.all()
    lookup_field = 'taxa_id'
    serializer_class = PfamListSerializer

    
    def get_queryset(self):
        taxa_id = self.kwargs['taxa_id']
        return Domain.objects.filter(taxa_id__taxa_id = taxa_id)

class CoverageDetails(mixins.RetrieveModelMixin,
                      generics.GenericAPIView):
    queryset = Protein.objects.all()
    lookup_field = 'protein_id'
    serializer_class = CoverageSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)





