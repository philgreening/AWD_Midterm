import json
from django.conf.urls import url
from django.test import TestCase, client
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import  APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from .models import *

# Create your tests here.

class ProteinTest(APITestCase):
    def test_ProteinDetailReturnSuccess(self):
        protein = ProteinFactory.create(pk=1, protein_id = 'XYZ87')
        url = reverse('protein_api', kwargs= {'protein_id' : 'XYZ87' })
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)
