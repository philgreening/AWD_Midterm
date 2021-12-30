import os
import sys
import django
import csv
from collections import defaultdict

# sys.path.append("/home/coder/project/topic2/bioweb")
#AWD_Midterm/proteinAPI
sys.path.append('/home/philgreening/AWD_Midterm/proteinAPI')


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'proteinAPI.settings')
django.setup()

from proteinData.models import *

sequences_data_file =  '/home/philgreening/AWD_Midterm/proteinAPI/data/assignment_data_sequences.csv'
pfam_desc_data_file = '/home/philgreening/AWD_Midterm/proteinAPI/data/pfam_descriptions.csv'
protein_dataset_file = '/home/philgreening/AWD_Midterm/proteinAPI/data/assignment_data_set.csv'

#sequencing = defaultdict(list)
sequencing = set() 
# pfam_descriptions = defaultdict(list)
pfam_descriptions = set()
proteins = defaultdict(list)

with open(sequences_data_file) as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       for row in csv_reader:
              #sequencing[row[0]] = row[0+1]
              sequencing.add((row[0], row[1]))


with open(pfam_desc_data_file) as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       for row in csv_reader:
              # pfam_descriptions[row[0]] = row[0+1]
              pfam_descriptions.add((row[0], row[1]))

with open(protein_dataset_file) as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       c = 0
       for row in csv_reader:
              #if ' ' in row[3]:
              row[3:4] = row[3].split(' ', maxsplit=1)
              # for entry in org:
              #        tupple = org.split(" ")
              #        proteins[row[3]][tupple[0]] = tupple[1]
              proteins[row[0]] = row[0:10]
              c += 1
       print(row[3])
       print(row[4])
       print(proteins[row[0]])
       print(c)


Protein.objects.all().delete()
Sequencing.objects.all().delete()
PfamDescriptions.objects.all().delete()
Organism.objects.all().delete()
Domain.objects.all().delete()


# for entry in sequencing:
#     row = Sequencing.objects.create(protein_id = entry[0], sequence = entry[1])
#     row.save()

sequencing_row = {}
pfam_desc_row = {}
domain_row = {}
organism_row = {}
protein_row = {}

# for protein_id, sequence, in sequencing.items():
#        row = Sequencing.objects.create(protein_id = protein_id, sequence = sequence)
#        #  row = Sequencing.objects.bulk_create(protein_id, sequence = sequence)
#        row.save()
#        sequencing_row[protein_id] = row
#        #print(protein_row[protein_id])
# #print(sequencing_row)

for seq in sequencing:
       row = Sequencing.objects.create(protein_id = seq[0],
                                       sequence = seq[1])
       row.save()
       sequencing_row[seq[0]] = row
       # print(row)


# for domain_id, pfam_desc, in pfam_descriptions.items():
#        row = PfamDescriptions.objects.create(domain_id = domain_id, pfam_desc = pfam_desc)
#        row.save()
#        pfam_desc_row[domain_id] = row
#        # print(pfam_desc_row[pfam_id])

for entry in pfam_descriptions:
       row = PfamDescriptions.objects.create(domain_id = entry[0],
                                             domain_description = entry[1])
       row.save()
       pfam_desc_row[entry[0]] = row
       # print(pfam_desc_row[pfam_id])

for protein_id, data in proteins.items():
       row = Organism.objects.create(protein_id = protein_id,
                                     taxa_id = data[1],
                                     clade = data[2],
                                     genus = data[3],
                                     species = data[4])
       row.save()
       organism_row[protein_id] = row

for protein_id, data in proteins.items():
       try:
              # row = Protein.objects.create(protein_id = protein_id,
              #               sequence = sequencing_row[protein_id],
              #               org_taxa_id = data[1],
              #               org_clade = data[2],
              #               org_genus = data[3],
              #               org_species = data[4],
              #               domain_id = data[6],
              #               pfam_desc = pfam_desc_row[data[6]], 
              #               domain_desc = data[5],
              #               domain_start_coord = data[7],
              #               domain_end_coord = data[8],
              #               protein_length = data[9] 
              #               )
              row = Protein.objects.create(protein_id = protein_id,
                                           taxonomy = organism_row[protein_id],
                                           sequence = sequencing_row[protein_id],
                                           length = data[9])

              #row.save()
       except KeyError:
              # print(protein_id + " : " + "No sequence matched")
              # row.sequence = None
              # row = Protein.objects.create(protein_id = protein_id,
              #               sequence = None,
              #               org_taxa_id = data[1],
              #               org_clade = data[2],
              #               org_genus = data[3],
              #               org_species = data[4],
              #               domain_id = data[6],
              #               pfam_desc = pfam_desc_row[data[6]], 
              #               domain_desc = data[5],
              #               domain_start_coord = data[7],
              #               domain_end_coord = data[8],
              #               protein_length = data[9] 
              #               )
              row = Protein.objects.create(protein_id = protein_id,
                                           taxonomy = organism_row[protein_id],
                                           sequence = None,
                                           length = data[9])
       row.save()
       protein_row[protein_id] = row




for protein_id, data in proteins.items():
       row = Domain.objects.create(protein_id = protein_row[protein_id],
                                   pfam_id = pfam_desc_row[data[6]], 
                                   domain_id = data[6],
                                   description = data[5],
                                   start = data[7],
                                   end = data[8])
       row.save()


# data_file = '/home/coder/project/topic2/scripts/example_data_to_load.csv'
# data_file = '/home/dbuchan/Course_Dev/docker_containers/adv_web_dev_topic_3_docker/files/topic2/example_data_to_load.csv'
# genes = defaultdict(list)
# sequencing = set()
# ec = set()
# products = defaultdict(dict)
# attributes = defaultdict(dict)

# with open(data_file) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     header = csv_reader.__next__()
#     for row in csv_reader:
#         product_pairs = row[9].split(';')
#         attribute_pairs = row[10].split(';')
#         for pair in product_pairs:
#             tupple = pair.split(":")
#             products[row[0]][tupple[0]] = tupple[1]
#         for pair in attribute_pairs:
#             tupple = pair.split(":")
#             attributes[row[0]][tupple[0]] = tupple[1]
#         ec.add(row[8])
#         sequencing.add((row[4], row[5]))
#         genes[row[0]] = row[1:4]+row[6:9]

# GeneAttributeLink.objects.all().delete()
# Gene.objects.all().delete()
# EC.objects.all().delete()
# Sequencing.objects.all().delete()
# Attribute.objects.all().delete()
# Product.objects.all().delete()

# ec_rows = {}
# sequencing_rows = {}
# gene_rows = {}

# for entry in ec:
#     row = EC.objects.create(ec_name=entry)
#     row.save()
#     ec_rows[entry] = row
# for seq_centre in sequencing:
#     row = Sequencing.objects.create(sequencing_factory=seq_centre[0],
#                                     factory_location=seq_centre[1])
#     row.save()
#     sequencing_rows[seq_centre[0]] = row
# for gene_id, data in genes.items():
#     row = Gene.objects.create(gene_id=gene_id, entity=data[0],
#                               start=data[1], stop=data[2],
#                               sense=data[3], start_codon=data[4],
#                               sequencing=sequencing_rows['Sanger'],
#                               ec=ec_rows[data[5]])
#     row.save()
#     gene_rows[gene_id] = row

# for gene_id, data_dict in products.items():
#     for key in data_dict.keys():
#         row = Product.objects.create(type=key, product=data_dict[key],
#                                      gene=gene_rows[gene_id])
#         row.save()

# for gene_id, data_dict in attributes.items():
#     for key in data_dict.keys():
#         row = Attribute.objects.create(key=key, value=data_dict[key])
#         row.gene.add(gene_rows[gene_id])
#         row.save()
