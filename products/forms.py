from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label='Nombre')
    description = forms.CharField(max_length=300, label='Descripción')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')
    available = forms.BooleanField(
        initial=True, label='Disponible', required=False)
    photo = forms.ImageField(label='Foto', required=False)

    def save(self):
        from .models import Product
        data = self.cleaned_data
        Product.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            available=data['available'],
            photo=data.get('photo')  # usa `.get()` por si es None
        )
