from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Vendedor
from .serializers import VendedorSerializer
import json
from django.core.exceptions import ObjectDoesNotExist

@api_view(["GET"])
def get_vendedores(request):
  vendedores = Vendedor.objects.all()
  serializer = VendedorSerializer(vendedores, many=True)
  return JsonResponse({'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
  
@api_view(["GET"])
def get_vendedor(request, vendedor_id):
  try:
    vendedor = Vendedor.objects.get(pk=vendedor_id)
    serializer = VendedorSerializer(vendedor)
    return JsonResponse({'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def add_vendedor(request):
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

@api_view(["PUT"])
def update_vendedor(request, vendedor_id):
  try:
    vendedor = Vendedor.objects.get(pk=vendedor_id)
    serializer = VendedorSerializer(vendedor, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse({'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
    else:
      return JsonResponse({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_vendedor(request, vendedor_id):
  try:
    vendedor = Vendedor.objects.get(id=vendedor_id)
    vendedor.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception as e:
    print(e)
    return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
