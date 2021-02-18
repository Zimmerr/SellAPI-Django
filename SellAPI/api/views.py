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
  return JsonResponse({'vendedores': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def add_vendedor(request):
  payload = json.loads(request.body)
  try:
    vendedor = Vendedor.objects.create(
      nome=payload["nome"],
      data_nasc=payload["data_nasc"], #TODO: Formatar a data de DD/MM/YYYY pra YYYY-MM-DD
    )
    serializer = VendedorSerializer(vendedor)
    return JsonResponse({'vendedores': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_vendedor(request, vendedor_id):
  payload = json.loads(request.body)
  try:
    vendedor_item = Vendedor.objects.filter(id=vendedor_id)
    # returns 1 or 0
    vendedor_item.update(**payload)
    vendedor = Vendedor.objects.get(id=vendedor_id)
    serializer = VendedorSerializer(vendedor)
    return JsonResponse({'vendedor': serializer.data}, safe=False, status=status.HTTP_200_OK)
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
