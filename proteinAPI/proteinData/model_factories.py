import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File
from random import randint

from factory.base import Factory

from .models import *

# create fixtures for sequencing model
class SequencingFactory(factory.django.DjangoModelFactory):
    protein_id = 'PROTEIN123'
    sequence = 'TESTSEQUENCE'

    class Meta:
        model = Sequencing

# create fixtures for pfamDescriptions model
class PfamDescriptionFactory(factory.django.DjangoModelFactory):
    domain_id = 'PF12345'
    domain_description = 'PeptidaseC13family'

    class Meta:
        model = PfamDescriptions

# create fixtures for protein model
class ProteinFactory(factory.django.DjangoModelFactory):
    protein_id = 'PROTEIN123'
    sequence = factory.SubFactory(SequencingFactory)
    taxa_id = '12345'
    clade = 'E'
    genus = factory.Faker('sentence', nb_words = 1)
    species = factory.Faker('sentence', nb_words = 1)
    length =  randint(0,4000)

    class Meta:
        model = Protein

# create fixtures for domain model
class DomainFactory(factory.django.DjangoModelFactory):
    protein_id = factory.SubFactory(ProteinFactory)
    taxa_id = factory.SubFactory(ProteinFactory)
    pfam_id = factory.SubFactory(PfamDescriptionFactory)
    domain_id = 'PF12345'
    description = factory.Faker('sentence', nb_words = 3)
    start = randint(1, 1000)
    stop = start+randint(1, 1000)

    class Meta:
        model = Domain


