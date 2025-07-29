from django.views.generic.edit import FormView
from django.views.generic import ListView  # Opción 1 (recomendada)
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product  # Asegúrate de importar el modelo Product


class ProductFormView(FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductList(ListView):
    model = Product
    template_name = "products/list_product.html"
    # Ahora usarás 'products' en lugar de 'object_list'
    context_object_name = 'products'

    def get_queryset(self):
        print(Product.objects.all())  # Verifica qué se está consultando
        return super().get_queryset()
