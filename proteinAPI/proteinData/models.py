from django.db import models

# model for sequencing table
class Sequencing(models.Model):
    protein_id = models.CharField(max_length=10, null=False, blank=False)
    sequence = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.sequence

# model for protein table. Foreign key sequence references sequencing table
class Protein(models.Model):
    protein_id = models.CharField(max_length=10, null=False, blank=False)
    sequence = models.ForeignKey(Sequencing, null=True, blank= True, on_delete=models.DO_NOTHING)
    taxa_id = models.IntegerField(null=False, blank=False)
    clade = models.CharField(max_length=1, null=False)
    genus = models.CharField(max_length=256, null=False, blank=False)
    species = models.CharField(max_length=256, null=False, blank=False)
    length = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.protein_id

# model for pfam description table
class PfamDescriptions(models.Model):
    domain_id = models.CharField(max_length=256, null=False, blank=False)
    domain_description = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.domain_description

# model for domain table. Foreign key 'protein_id' and 'taxa_id' references protein model,
#  'pfam_id' references pfamDescriptions model   
class Domain(models.Model):
    protein_id = models.ForeignKey(Protein, null=False, blank= False, related_name='domains', on_delete=models.CASCADE)
    taxa_id = models.ForeignKey(Protein, null=False, blank= False, on_delete=models.CASCADE)
    pfam_id = models.ForeignKey(PfamDescriptions, on_delete=models.DO_NOTHING)
    domain_id = models.CharField(max_length=256, null=False, blank=False)
    description = models.CharField(max_length=256, null=False, blank=False)
    start = models.IntegerField(null=False, blank=False)
    stop = models.IntegerField(null=False, blank=False)
    #length = models.ForeignKey(Protein, null=False, blank=False, related_name= 'protein_length', on_delete=models.CASCADE )

    def __str__(self):
        return self.protein_id

    



