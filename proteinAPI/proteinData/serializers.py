from django.db.models import fields
from rest_framework import serializers
from .models import *

class ProteinSerializer(serializers.Serializer):
    class Meta:
        model = Protein
        fields = ['protein_id', 'sequence', 'org_taxa_id',
                 'org_clade', 'org_genus', 'org_species',
                 'domain_id', 'pfam_desc', 'domain_desc',
                 'domain_start_coord', 'domain_end_coord',
                 'protein_length']

