import json
from django.conf.urls import url
from django.test import TestCase, client
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import  APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from .models import *
from .serializers import *

#***************************************
#***************API TESTS***************
#***************************************


# tests /api/protein endpoint
class ProteinTest(APITestCase):
    protein1 = None
    protein2 = None
    good_url = ''
    bad_url = ''

    # set up variables for testing
    def setUp(self):
        self.protein1 = ProteinFactory.create()
        self.good_url = reverse('protein_api', kwargs= {'protein_id' : 'PROTEIN123' })
        self.bad_url = '/api/protein/1'

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        Sequencing.objects.all().delete()
        PfamDescriptions.objects.all().delete()
        Protein.objects.all().delete()
        Domain.objects.all().delete()

        SequencingFactory.reset_sequence(0)
        PfamDescriptionFactory.reset_sequence(0)
        ProteinFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)

    def test_ProteinDetailReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
    
    def test_ProteinDetailReturnFailOnBadAttribute(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
    
    def test_ProteinDetailCheckFieldPresent(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        self.assertTrue('sequence' in data)



# tests /api/pfam endpoint
class PfamTest(APITestCase):
    domain = None
    good_url = ''
    bad_url = ''

    # set up variables for testing
    def setUp(self):
        self.domain = PfamDescriptionFactory.create()
        self.good_url = reverse('pfam_api', kwargs= {'domain_id' : 'PF12345' })
        self.bad_url = '/api/pfam/1'
    
    # Deletes everything from test database and resets primary key
    def tearDown(self):
        Sequencing.objects.all().delete()
        PfamDescriptions.objects.all().delete()
        Protein.objects.all().delete()
        Domain.objects.all().delete()

        SequencingFactory.reset_sequence(0)
        PfamDescriptionFactory.reset_sequence(0)
        ProteinFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)
    
    def test_PfamDetailReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_PfamDetailReturnFailOnBadAttribute(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_PfamDetailCheckFieldPresent(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        self.assertTrue('domain_description' in data)


# tests /api/proteins endpoint
class ProteinsTest(APITestCase):
    protein = None
    protein2 = None
    protein3 = None
    good_url = ''
    bad_url = ''

    # set up variables for testing
    def setUp(self):
        self.protein = ProteinFactory.create()
        self.protein2 = ProteinFactory.create(pk=2, protein_id = 'PROTEIN456' )
        self.protein3 = ProteinFactory.create(pk=3, protein_id = 'PROTEIN789')
        self.good_url = reverse('proteins_api', kwargs= {'taxa_id' : '12345' })
        self.bad_url = '/api/proteins/'
    
    # Deletes everything from test database and resets primary key
    def tearDown(self):
        Sequencing.objects.all().delete()
        PfamDescriptions.objects.all().delete()
        Protein.objects.all().delete()
        Domain.objects.all().delete()

        SequencingFactory.reset_sequence(0)
        PfamDescriptionFactory.reset_sequence(0)
        ProteinFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)
    
    def test_ProteinsListReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
    
    def test_ProteinsListReturnFailOnBadAttribute(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
 
    def test_ProteinsListLength(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        self.assertEqual(len(data), 3)
    
    def test_ProteinsListCheckFieldPresent(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        for protein in data:
            self.assertTrue('protein_id' in protein)

# tests /api/pfams endpoint
class DomainsTest(APITestCase):
    domain = None
    domain2 = None
    domain3 = None
    good_url = ''
    bad_url = ''

    # set up variable for testing
    def setUp(self):
        self.protein = DomainFactory.create()
        self.protein2 = DomainFactory.create(pk=2, domain_id = 'PF67890' )
        self.protein3 = DomainFactory.create(pk=3, domain_id = 'PF54321')
        self.good_url = reverse('pfams_api', kwargs= {'taxa_id' : '12345' })
        self.bad_url = '/api/pfams/'
    
    # Deletes everything from test database and resets primary key
    def tearDown(self):
        Sequencing.objects.all().delete()
        PfamDescriptions.objects.all().delete()
        Protein.objects.all().delete()
        Domain.objects.all().delete()

        SequencingFactory.reset_sequence(0)
        PfamDescriptionFactory.reset_sequence(0)
        ProteinFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)
    
    def test_DomainListReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
    
    def test_DomainListReturnFailOnBadAttribute(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
 
    def test_DomainListLength(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        self.assertEqual(len(data), 3)

    def test_DomainListCheckFieldPresent(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        for domain in data:
            self.assertTrue('pfam_id' in domain)

# tests /api/coverage endpoint
class CoverageTest(APITestCase):
    domain = None
    good_url = ''
    bad_url = ''

    # set up variables for testing
    def setUp(self):
        self.protein = DomainFactory.create()
        self.good_url = reverse('coverage_api', kwargs= {'protein_id' : 'PROTEIN123'})
        self.bad_url = '/api/coverage/'
    
    # Deletes everything from test database and resets primary key
    def tearDown(self):
        Sequencing.objects.all().delete()
        PfamDescriptions.objects.all().delete()
        Protein.objects.all().delete()
        Domain.objects.all().delete()

        SequencingFactory.reset_sequence(0)
        PfamDescriptionFactory.reset_sequence(0)
        ProteinFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)
    
    def test_CoverageReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
    
    def test_CoverageListReturnFailOnBadAttribute(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_CoverageCheckFieldPresent(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        for coverage in data:
            self.assertTrue('coverage' in coverage)

#**********************************************
#***************SERIALIZER TESTS***************
#**********************************************

class ProteinSerializerTest(APITestCase):
    protein = None
    protein_serializer = None

    # set up variable for testing
    def setUp(self):
        self.protein = ProteinFactory.create()
        self.protein_serializer = ProteinSerializer(instance=self.protein)

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        Sequencing.objects.all().delete()
        PfamDescriptions.objects.all().delete()
        Protein.objects.all().delete()
        Domain.objects.all().delete()

        SequencingFactory.reset_sequence(0)
        PfamDescriptionFactory.reset_sequence(0)
        ProteinFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)
    
    def test_ProteinSerializer(self):
        data = self.protein_serializer.data
        self.assertEqual(set(data.keys()), set(['protein_id', 'sequence',
                                                'taxonomy', 'length',
                                                'domains']))
    def test_ProteinSerializerProteinIdisOk(self):
        data = self.protein_serializer.data
        self.assertEqual(data['protein_id'], 'PROTEIN123')

class PfamSerializerTest(APITestCase):
    domain = None
    pfam_serializer = None

    # set up variable for testing  
    def setUp(self):
        self.domain = PfamDescriptionFactory.create()
        self.pfam_serializer = PfamSerializer(instance=self.domain)

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        Sequencing.objects.all().delete()
        PfamDescriptions.objects.all().delete()
        Protein.objects.all().delete()
        Domain.objects.all().delete()

        SequencingFactory.reset_sequence(0)
        PfamDescriptionFactory.reset_sequence(0)
        ProteinFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)
    
    def test_PfamSerializer(self):
        data = self.pfam_serializer.data
        self.assertEqual(set(data.keys()), set(['domain_id', 'domain_description']))

    def test_PfamSerializerDomainIdisOk(self):
        data = self.pfam_serializer.data
        self.assertEqual(data['domain_id'], 'PF12345')

class DomainSerializerTest(APITestCase):
    domain = None
    domain_serializer = None
    
    # set up variable for testing
    def setUp(self):
        self.domain = DomainFactory.create()
        self.pfam_serializer = DomainSerializer(instance=self.domain)

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        Sequencing.objects.all().delete()
        PfamDescriptions.objects.all().delete()
        Protein.objects.all().delete()
        Domain.objects.all().delete()

        SequencingFactory.reset_sequence(0)
        PfamDescriptionFactory.reset_sequence(0)
        ProteinFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)
    
    def test_DomainSerializer(self):
        data = self.pfam_serializer.data
        self.assertEqual(set(data.keys()), set(['pfam_id', 'description',
                                                'start', 'stop']))

class TaxonomySerializerTest(APITestCase):
    protein = None
    taxonomy_serializer = None

    # set up variable for testing
    def setUp(self):
        self.protein = ProteinFactory.create()
        self.taxonomy_serializer = TaxonomySerializer(instance=self.protein)

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        Sequencing.objects.all().delete()
        PfamDescriptions.objects.all().delete()
        Protein.objects.all().delete()
        Domain.objects.all().delete()

        SequencingFactory.reset_sequence(0)
        PfamDescriptionFactory.reset_sequence(0)
        ProteinFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)
    
    def test_TaxonomySerializer(self):
        data = self.taxonomy_serializer.data
        self.assertEqual(set(data.keys()), set(['taxa_id', 'clade',
                                                'genus', 'species']))

    def test_TaxonomySerializerTaxaIdisOk(self):
        data = self.taxonomy_serializer.data
        self.assertEqual(data['taxa_id'], 12345)

class ProteinListSerializerTest(APITestCase):
    protein = None
    proteinlist_serializer = None
    
    # set up variable for testing
    def setUp(self):
        self.protein = ProteinFactory.create()
        self.proteinlist_serializer = ProteinListSerializer(instance=self.protein)

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        Sequencing.objects.all().delete()
        PfamDescriptions.objects.all().delete()
        Protein.objects.all().delete()
        Domain.objects.all().delete()

        SequencingFactory.reset_sequence(0)
        PfamDescriptionFactory.reset_sequence(0)
        ProteinFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)
    
    def test_ProteinListSerializer(self):
        data = self.proteinlist_serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'protein_id']))

    def test_ProteinListSerializerProteinIdisOk(self):
        data = self.proteinlist_serializer.data
        self.assertEqual(data['protein_id'], 'PROTEIN123')

class PfamListSerializerTest(APITestCase):
    domain = None
    pfamlist_serializer = None
    
    # set up variable for testing
    def setUp(self):
        self.domain = DomainFactory.create()
        self.pfamlist_serializer = PfamListSerializer(instance=self.domain)

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        Sequencing.objects.all().delete()
        PfamDescriptions.objects.all().delete()
        Protein.objects.all().delete()
        Domain.objects.all().delete()

        SequencingFactory.reset_sequence(0)
        PfamDescriptionFactory.reset_sequence(0)
        ProteinFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)
    
    def test_PfamListSerializer(self):
        data = self.pfamlist_serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'pfam_id']))

    def test_PfamListSerializerIdisOk(self):
        data = self.pfamlist_serializer.data
        self.assertEqual(data['id'], 1)

class CoveragetSerializerTest(APITestCase):
    coverage = None
    coverage_serializer = None

    # set up variable for testing
    def setUp(self):
        self.coverage = DomainFactory.create()
        self.coverage_serializer = CoverageSerializer(instance=self.coverage)

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        Sequencing.objects.all().delete()
        PfamDescriptions.objects.all().delete()
        Protein.objects.all().delete()
        Domain.objects.all().delete()

        SequencingFactory.reset_sequence(0)
        PfamDescriptionFactory.reset_sequence(0)
        ProteinFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)
    
    def test_CoverageSerializer(self):
        data = self.coverage_serializer.data
        self.assertEqual(set(data.keys()), set(['coverage']))


