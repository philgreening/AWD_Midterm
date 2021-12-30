from django.db.models import fields
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

class DomainSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ['protein_id', 'org_taxa_id', 'org_clade', 'org_genus','org_species']

class OrganismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organism
        fields = ['protein_id', 
                  'domain_id', 'domain_desc',
                  'domain_start_coord', 'domain_end_coord',
                 ]

# class ProteinSerializer(serializers.ModelSerializer):
#     sequence = serializers.SlugRelatedField(read_only = True, slug_field='sequence')
#     pfam_desc = serializers.SlugRelatedField(read_only = True, slug_field='pfam_desc')
#     #org_genus = domainSerailizer()
#    # pfam_desc = PfamSerializer()
#     class Meta:
#         model = Protein
#        # lookup_field = 'protein_id'
#         fields = ['id', 'protein_id', 'sequence', 'org_taxa_id',
#                  'org_clade', 'org_genus', 'org_species',
#                  'domain_id', 'pfam_desc', 'domain_desc',
#                  'domain_start_coord', 'domain_end_coord',
#                  'protein_length']
#         # fields = ['id', 'protein_id', 'sequence',
#         #          'domain_id', 'pfam_desc', 'pfam_desc','domain_desc',
#         #          'domain_start_coord', 'domain_end_coord',
#         #          'protein_length']

class ProteinSerializer(serializers.ModelSerializer):
    sequence = serializers.SlugRelatedField(read_only = True, slug_field='sequence')
    #pfam_desc = serializers.SlugRelatedField(read_only = True, slug_field='pfam_desc')
    organism = OrganismSerializer(many = False, read_only = True)
   # pfam_desc = PfamSerializer()
    class Meta:
        model = Protein
       # lookup_field = 'protein_id'
        fields = ['id', 'protein_id', 'sequence', 'organism',
                 'protein_length']
        # fields = ['id', 'protein_id', 'sequence',
        #          'domain_id', 'pfam_desc', 'pfam_desc','domain_desc',
        #          'domain_start_coord', 'domain_end_coord',
        #          'protein_length']
