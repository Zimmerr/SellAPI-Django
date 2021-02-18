from django.urls import include, path
from . import views

urlpatterns = [
  path('getVendedores', views.get_vendedores),
  path('getVendedor/<int:vendedor_id>', views.get_vendedor),
  path('addVendedor', views.add_vendedor),
  path('updateVendedor/<int:vendedor_id>', views.update_vendedor),
  path('deleteVendedor/<int:vendedor_id>', views.delete_vendedor)
]