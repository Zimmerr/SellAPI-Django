import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Vendedor
from ..serializers import VendedorSerializer


client = Client()

class GetAllVendedoresTest(TestCase):
  def setUp(self):
    Vendedor.objects.create(
      nome='Thiago Neves', data_nasc='1975-05-12')
    Vendedor.objects.create(
      nome='Gerson', data_nasc='1995-08-27')
    Vendedor.objects.create(
      nome='Claudinho', data_nasc='1991-11-01')

  def test_get_all_vendedores(self):
    # get API response
    response = client.get('/api/vendedores')
    responseData = json.loads(response.content)['data']
    # get data from db
    puppies = Vendedor.objects.all()
    serializer = VendedorSerializer(puppies, many=True)
    responseSerializer = VendedorSerializer(responseData, many=True)
    self.assertEqual(responseSerializer.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetVendedorTest(TestCase):
    def setUp(self):
      self.thiago = Vendedor.objects.create(
        nome='Thiago Neves', data_nasc='1975-05-12')
      self.gerson = Vendedor.objects.create(
        nome='Gerson', data_nasc='1995-08-27')
      self.claudinho = Vendedor.objects.create(
        nome='Claudinho', data_nasc='1991-11-01')
        
    def test_get_vendedor_valido(self):
      response = client.get('/api/vendedores/' + str(self.gerson.pk))
      responseData = json.loads(response.content)['data']
      vendedor = Vendedor.objects.get(pk=self.gerson.pk)
      serializer = VendedorSerializer(vendedor)
      responseSerializer = VendedorSerializer(responseData)
      self.assertEqual(responseSerializer.data, serializer.data)
      self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_vendedor_invalido(self):
      response = client.get('/api/vendedores/' + str(999))
      self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateVendedorTest(TestCase):
    def setUp(self):
      self.valid_payload = {
        'nome': 'Thiago Neves',
        'data_nasc': '1995-05-30',
      }
      self.invalid_payload = {
        'name': '',
        'age': 4,
      }

    def test_create_valid_puppy(self):
        response = client.post(
            '/api/vendedores',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            '/api/vendedores',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateVendedorTest(TestCase):

  def setUp(self):
    self.thiago = Vendedor.objects.create(
      nome='Thiago Neves', data_nasc='1975-05-12')
    self.gerson = Vendedor.objects.create(
      nome='Gerson', data_nasc='1995-08-27')
    self.claudinho = Vendedor.objects.create(
      nome='Claudinho', data_nasc='1991-11-01')
    self.valid_payload = {
      'nome': 'Breno',
      'data_nasc': '1990-08-27',
    }
    self.invalid_payload = {
      'name': '',
      'age': 4,
    }

  def test_valid_update_puppy(self):
    response = client.put(
      '/api/vendedores/' + str(self.gerson.pk),
      data=json.dumps(self.valid_payload),
      content_type='application/json'
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    vendedor = Vendedor.objects.get(pk=self.gerson.pk)
    self.assertEqual(vendedor.nome, self.valid_payload.get('nome'))
    self.assertEqual(vendedor.data_nasc.strftime("%Y-%m-%d"), self.valid_payload.get('data_nasc'))

  def test_invalid_update_puppy(self):
    response = client.put(
      '/api/vendedores/' + str(self.gerson.pk),
      data=json.dumps(self.invalid_payload),
      content_type='application/json')
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteVendedorTest(TestCase):

  def setUp(self):
    self.thiago = Vendedor.objects.create(
      nome='Thiago Neves', data_nasc='1975-05-12')
    self.gerson = Vendedor.objects.create(
      nome='Gerson', data_nasc='1995-08-27')

  def test_valid_delete_vendedor(self):
      response = client.delete('/api/vendedores/' + str(self.gerson.pk))
      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_invalid_delete_vendedor(self):
      response = client.delete('/api/vendedores/' + str(999))
      self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)   