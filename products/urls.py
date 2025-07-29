from django.urls import path
from .views import ProductFormView, ProductList  # ¡Importa ambas clases!

urlpatterns = [
    path('', ProductList.as_view(), name="list_product"),
    path('agregar/', ProductFormView.as_view(), name='add_product'),
]
