from django.db import models

#create model for sequencing table
class Sequencing(models.Model):
    protein_id = models.CharField(max_length=10, null=False, blank=False)
    #sequence = models.CharField(max_length=40000, null=True, blank=True)
    sequence = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.sequence

#create model for pfam description table
class PfamDescriptions(models.Model):
    domain_id = models.CharField(max_length=256, null=False, blank=False)
    pfam_desc = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.pfam_desc

# #create model for protein table
# class Protein(models.Model):
#     protein_id = models.CharField(max_length=10, null=False, blank=False)
#     sequence = models.ForeignKey(Sequencing, null=True, blank= True, on_delete=models.DO_NOTHING)
#     org_taxa_id = models.IntegerField(null=False, blank=False)
#     org_clade = models.CharField(max_length=1, null=False)
#     org_genus = models.CharField(max_length=256, null=False, blank=False)
#     org_species = models.CharField(max_length=256, null=False, blank=False)
#     domain_id = models.CharField(max_length=256, null=False, blank=False)
#     pfam_desc = models.ForeignKey(PfamDescriptions, on_delete=models.DO_NOTHING)
#     domain_desc = models.CharField(max_length=256, null=False, blank=False)
#     domain_start_coord = models.IntegerField(null=False, blank=False)
#     domain_end_coord = models.IntegerField(null=False, blank=False)
#     protein_length = models.IntegerField(null=False, blank=False)

#     def __str__(self):
#         return self.protein_id



class Organism(models.Model):
    protein_id = models.CharField(max_length=10, null=False, blank=False)
    org_taxa_id = models.IntegerField(null=False, blank=False)
    org_clade = models.CharField(max_length=1, null=False)
    org_genus = models.CharField(max_length=256, null=False, blank=False)
    org_species = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.protein_id

class Domain(models.Model):
    protein_id = models.CharField(max_length=10, null=False, blank=False)
    domain_id = models.CharField(max_length=256, null=False, blank=False)
    domain_desc = models.CharField(max_length=256, null=False, blank=False)
    domain_start_coord = models.IntegerField(null=False, blank=False)
    domain_end_coord = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.protein_id

class Protein(models.Model):
    protein_id = models.CharField(max_length=10, null=False, blank=False)
    sequence = models.ForeignKey(Sequencing, null=True, blank= True, on_delete=models.DO_NOTHING)
    protein_length = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return self.protein_id



