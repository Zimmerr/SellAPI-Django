from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Vendedor
from .serializers import VendedorSerializer
import json
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET', 'POST'])
def get_all_post_vendedor(request):
  
  # Busca todos os vendedores
  if request.method == 'GET':
    vendedores = Vendedor.objects.all()
    serializer = VendedorSerializer(vendedores, many=True)
    return JsonResponse({'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
  
  # Insere um novo Vendedor
  if request.method == 'POST':
    try:
      vendedor = {
        'nome': request.data.get('nome'),
        'data_nasc': request.data.get('data_nasc') #TODO: tratamento de data (atualmente é obrigatório vir em formato YYYY-MM-DD)
      }
      serializer = VendedorSerializer(data=vendedor)
      if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
      else:
        return JsonResponse({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
      return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_vendedor(request, vendedor_id):
  try:
    vendedor = Vendedor.objects.get(pk=vendedor_id)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)

  # Busca UM vendedor com o ID especificado
  if request.method == 'GET':
    try:
      serializer = VendedorSerializer(vendedor)
      return JsonResponse({'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except Exception:
      return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  # Atualiza o vendedor do ID especificado
  if request.method == 'PUT':
    try:
      serializer = VendedorSerializer(vendedor, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
      else:
        return JsonResponse({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
      return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  # Deleta o vendedor do ID especificado
  elif request.method == 'DELETE':
    try:
      vendedor.delete()
      return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
      return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
