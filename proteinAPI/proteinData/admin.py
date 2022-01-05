from django.contrib import admin
from .models import *

class ProteinAdmin(admin.ModelAdmin):
    list_display = ['protein_id', 'sequence',
                    'taxa_id', 'clade', 'genus',
                     'species', 'length'] 

class SequencingAdmin(admin.ModelAdmin):
    list_display = ['protein_id', 'sequence']

class PfamDescriptionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'domain_description']

class DomainAdmin(admin.ModelAdmin):
    list_display = ['protein_id', 'taxa_id', 'pfam_id',
                    'domain_id', 'description',
                    'start', 'stop']

admin.site.register(Protein, ProteinAdmin)
admin.site.register(Sequencing, SequencingAdmin)
admin.site.register(PfamDescriptions, PfamDescriptionsAdmin)
admin.site.register(Domain, DomainAdmin)