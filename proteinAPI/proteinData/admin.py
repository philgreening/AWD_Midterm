from django.contrib import admin
from .models import *

# class ProteinAdmin(admin.ModelAdmin):
#     list_display = ['protein_id', 'sequence', 'org_taxa_id',
#                  'org_clade', 'org_genus', 'org_species',
#                  'domain_id', 'pfam_desc', 'domain_desc',
#                  'domain_start_coord', 'domain_end_coord',
#                  'protein_length']

class ProteinAdmin(admin.ModelAdmin):
    list_display = ['protein_id', 'sequence', 'taxonomy',
                    'length'
                   ] 

class SequencingAdmin(admin.ModelAdmin):
    list_display = ['protein_id', 'sequence']

class PfamDescriptionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'domain_description']

class OrganismAdmin(admin.ModelAdmin):
    list_display = ['protein_id', 'taxa_id',
                    'clade', 'genus', 'species',
                    ]

class DomainAdmin(admin.ModelAdmin):
    list_display = ['protein_id', 'taxa_id', 'pfam_id',
                    'domain_id', 'description',
                    'start', 'end',
                   ]

admin.site.register(Protein, ProteinAdmin)
admin.site.register(Sequencing, SequencingAdmin)
admin.site.register(PfamDescriptions, PfamDescriptionsAdmin)
admin.site.register(Organism, OrganismAdmin)
admin.site.register(Domain, DomainAdmin)