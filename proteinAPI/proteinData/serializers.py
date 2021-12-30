from typing import Sequence
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import *

class SequencingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequencing
        fields = ['id', 'protein_id', 'sequence']

class PfamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PfamDescriptions
        fields = ['id', 'domain_id', 'pfam_desc']

class domainSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ['protein_id', 'org_taxa_id', 'org_clade', 'org_genus','org_species']

class ProteinSerializer(serializers.ModelSerializer):
    sequence = serializers.SlugRelatedField(read_only = True, slug_field='sequence')
    pfam_desc = serializers.SlugRelatedField(read_only = True, slug_field='pfam_desc')
    #org_genus = domainSerailizer()
   # pfam_desc = PfamSerializer()
    class Meta:
        model = Protein
       # lookup_field = 'protein_id'
        fields = ['id', 'protein_id', 'sequence', 'org_taxa_id',
                 'org_clade', 'org_genus', 'org_species',
                 'domain_id', 'pfam_desc', 'domain_desc',
                 'domain_start_coord', 'domain_end_coord',
                 'protein_length']
        # fields = ['id', 'protein_id', 'sequence',
        #          'domain_id', 'pfam_desc', 'pfam_desc','domain_desc',
        #          'domain_start_coord', 'domain_end_coord',
        #          'protein_length']
