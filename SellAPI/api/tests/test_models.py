from django.test import TestCase
from ..models import Vendedor

# Create your tests here.

class VendedorTest(TestCase):
  """ Test module for Vendedor model """

  def setUp(self):
    Vendedor.objects.create(
      nome='Thiago Neves', data_nasc='1975-05-12')
    Vendedor.objects.create(
      nome='Gerson', data_nasc='1995-08-27')

  def test_vendedor(self):
    thiago = Vendedor.objects.get(nome='Thiago Neves')
    gerson = Vendedor.objects.get(nome='Gerson')
    self.assertEqual(
      thiago.__str__(), "Thiago Neves")
    self.assertEqual(
      gerson.__str__(), "Gerson")