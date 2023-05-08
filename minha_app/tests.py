from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class MinhaAppTests(TestCase):
    def test_pagina_inicial(self):
        response = self.client.get(reverse('minha_func'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Meu App')
