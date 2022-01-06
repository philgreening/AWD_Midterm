import os
import sys
import django
import csv
from collections import defaultdict
from pathlib import Path


#sys.path.append('/home/philgreening/AWD_Midterm/proteinAPI')
sys.path.append('../../AWD_Midterm/proteinAPI')


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'proteinAPI.settings')
django.setup()

from proteinData.models import *

# sequences_data_file =  '/home/philgreening/AWD_Midterm/proteinAPI/data/assignment_data_sequences.csv'
sequences_data_file =  Path(__file__).parent / '../../../AWD_Midterm/proteinAPI/data/assignment_data_sequences.csv'
#pfam_desc_data_file = '/home/philgreening/AWD_Midterm/proteinAPI/data/pfam_descriptions.csv'
pfam_desc_data_file = Path(__file__).parent / '../../../AWD_Midterm/proteinAPI/data/pfam_descriptions.csv'
#protein_dataset_file = '../../../home/philgreening/AWD_Midterm/proteinAPI/data/assignment_data_set.csv'
protein_dataset_file = Path(__file__).parent / '../../../AWD_Midterm/proteinAPI/data/assignment_data_set.csv'

# variables to hold data
sequencing = set() 
pfam_descriptions = set()
proteins = defaultdict(list)

# Reads sequence data csv file
with open(sequences_data_file) as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       for row in csv_reader:
              sequencing.add((row[0], row[1]))

# Reads pfam descriptions csv file
with open(pfam_desc_data_file) as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       for row in csv_reader:
              pfam_descriptions.add((row[0], row[1]))

# Reads pfam descriptions csv file
with open(protein_dataset_file) as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       lines = 0
       for row in csv_reader:
              #splits row 3 into genus and species fields
              row[3:4] = row[3].split(' ', maxsplit=1)
              proteins[row[0]] = row[0:10]
       print('Protein - Check split csv row: ' + row[3] + ' : ' + row[4] )
       print('Protein - Check first row fields: ' + str(proteins[row[0]]))

# clears database before database entries created
Protein.objects.all().delete()
Sequencing.objects.all().delete()
PfamDescriptions.objects.all().delete()
Domain.objects.all().delete()

# Variables to pass data to other models
sequencing_row = {}
pfam_desc_row = {}
domain_row = {}
protein_row = {}

# creates database entries in sequencing model
for seq in sequencing:
       row = Sequencing.objects.create(protein_id = seq[0],
                                       sequence = seq[1])
       row.save()
       sequencing_row[seq[0]] = row

# creates database entries in pfamDescription model
for entry in pfam_descriptions:
       row = PfamDescriptions.objects.create(domain_id = entry[0],
                                             domain_description = entry[1])
       row.save()
       pfam_desc_row[entry[0]] = row

# creates database entries in protein model
for protein_id, data in proteins.items():
       #if unable to match sequence data to protein_id, Null is added to sequence
       try:
              row = Protein.objects.create(protein_id = protein_id,
                                           sequence = sequencing_row[protein_id],
                                           taxa_id = data[1],
                                           clade = data[2],
                                           genus = data[3],
                                           species = data[4],
                                           length = data[9])
       except KeyError:
              row = Protein.objects.create(protein_id = protein_id,
                                           sequence = None,
                                           taxa_id = data[1],
                                           clade = data[2],
                                           genus = data[3],
                                           species = data[4],
                                           length = data[9])
       row.save()
       protein_row[protein_id] = row

# creates database entries in domain model
for protein_id, data in proteins.items():
       row = Domain.objects.create(protein_id = protein_row[protein_id],
                                   taxa_id = protein_row[protein_id],
                                   pfam_id = pfam_desc_row[data[6]], 
                                   domain_id = data[6],
                                   description = data[5],
                                   start = data[7],
                                   stop = data[8])
       row.save()
       domain_row[protein_id] = row