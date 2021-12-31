from django.db import models
from django.db.models.deletion import DO_NOTHING

#create model for sequencing table
class Sequencing(models.Model):
    protein_id = models.CharField(max_length=10, null=False, blank=False)
    #sequence = models.CharField(max_length=40000, null=True, blank=True)
    sequence = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.sequence

class Organism(models.Model):
    protein_id = models.CharField(max_length=10, null=False, blank=False)
    #protein_id = models.ForeignKey(Protein, null=False, blank= False, related_name='taxonomy', on_delete=models.DO_NOTHING)
    taxa_id = models.IntegerField(null=False, blank=False)
    clade = models.CharField(max_length=1, null=False)
    genus = models.CharField(max_length=256, null=False, blank=False)
    species = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.protein_id

class Protein(models.Model):
    protein_id = models.CharField(max_length=10, null=False, blank=False)
    taxonomy = models.ForeignKey(Organism, null= False, blank= False, on_delete=models.DO_NOTHING)
    sequence = models.ForeignKey(Sequencing, null=True, blank= True, on_delete=models.DO_NOTHING)
    length = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return self.protein_id

#create model for pfam description table
class PfamDescriptions(models.Model):
    domain_id = models.CharField(max_length=256, null=False, blank=False)
    domain_description = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.domain_description


class Domain(models.Model):
   # protein_id = models.CharField(max_length=10, null=False, blank=False)
    protein_id = models.ForeignKey(Protein, null=False, blank= False, related_name='domains', on_delete=models.DO_NOTHING)
    taxa_id = models.ForeignKey(Organism, null=False, blank= False, on_delete=DO_NOTHING)
    pfam_id = models.ForeignKey(PfamDescriptions, on_delete=models.DO_NOTHING)
    domain_id = models.CharField(max_length=256, null=False, blank=False)
    description = models.CharField(max_length=256, null=False, blank=False)
    start = models.IntegerField(null=False, blank=False)
    end = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.protein_id



