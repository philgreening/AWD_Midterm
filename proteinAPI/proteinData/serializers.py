from rest_framework import serializers
from .models import *

class SequencingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequencing
        fields = ['id', 'protein_id', 'sequence']

class PfamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PfamDescriptions
        fields = ['id', 'domain_id', 'domain_description']

class OrganismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organism
        fields = ['protein_id', 'taxa_id', 'clade', 'genus', 'species']

class DomainSerializer(serializers.ModelSerializer):
    pfam_id = PfamSerializer()

    class Meta:
        model = Domain
        fields = ['pfam_id','protein_id', 
                  'domain_id', 'description',
                  'start', 'end',
                 ]

class ProteinSerializer(serializers.ModelSerializer):
    sequence = serializers.SlugRelatedField(read_only = True, slug_field='sequence')
    taxonomy = OrganismSerializer()
    domains = DomainSerializer(many = True)

    class Meta:
        model = Protein
        fields = ['id', 'protein_id', 'sequence', 'taxonomy',
                 'length', 'domains']

class ProteinListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organism
        fields = ['id', 'protein_id']
