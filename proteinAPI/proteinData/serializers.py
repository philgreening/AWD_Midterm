from rest_framework import serializers
from .models import *


class PfamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PfamDescriptions
        fields = ['domain_id', 'domain_description']


class DomainSerializer(serializers.ModelSerializer):
    # Creates nested JSON, pfam details inside domains
    pfam_id = PfamSerializer()

    class Meta:
        model = Domain
        fields = ['pfam_id', 'description',
                  'start', 'stop']
                 
class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ['taxa_id', 'clade', 'genus', 'species']


class ProteinSerializer(serializers.ModelSerializer):
    #references sequence field
    sequence = serializers.SlugRelatedField(read_only = True, slug_field='sequence')

    # Creates Nested JSON,  taxonomy and domain information inside protein details
    taxonomy = TaxonomySerializer(source = '*')
    domains = DomainSerializer(many = True)

    class Meta:
        model = Protein
        fields = ['protein_id', 'sequence',
                  'taxonomy', 'length', 'domains']

class ProteinListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ['id', 'protein_id']

class PfamListSerializer(serializers.ModelSerializer):
    pfam_id = PfamSerializer()

    class Meta:
        model = Domain
        fields = ['id', 'pfam_id']


class CoverageSerializer(serializers.ModelSerializer):
    # creates custom coverage field and call get_coverage method
    coverage = serializers.SerializerMethodField('get_coverage')

    class Meta:
        model = Domain
        fields = ['coverage']

    # calculates and returns domain coverage 
    def get_coverage(self, obj):
        length = obj.protein_id.length
        start = obj.start
        stop = obj.stop
        coverage = (start-stop)/length
        return coverage
    

