from django.urls import include, path
from . import views

urlpatterns = [
  path('vendedores', views.get_all_post_vendedor),
  path('vendedores/<int:vendedor_id>', views.get_delete_update_vendedor),
  path('vendedores/aniversariantes/<int:mes>', views.get_vendedores_aniversariantes_mes)
]