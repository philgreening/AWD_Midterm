from django.contrib import admin
from .models import *

class ProteinAdmin(admin.ModelAdmin):
    list_display = ['protein_id', 'sequence', 'org_taxa_id',
                 'org_clade', 'org_genus', 'org_species',
                 'domain_id', 'pfam_desc', 'domain_desc',
                 'domain_start_coord', 'domain_end_coord',
                 'protein_length']
                 
class SequencingAdmin(admin.ModelAdmin):
    list_display = ['protein_id', 'sequence']

class PfamDescriptionsAdmin(admin.ModelAdmin):
    list_display = ['domain_id', 'pfam_desc']

admin.site.register(Protein, ProteinAdmin)
admin.site.register(Sequencing, SequencingAdmin)
admin.site.register(PfamDescriptions, PfamDescriptionsAdmin)