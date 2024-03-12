from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    id = forms.IntegerField(required=True)
    precio = forms.IntegerField(required=True)
    descripcion = forms.CharField(max_length=255, required=True)

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    apellido = forms.CharField(max_length=60, required=True)
    email = forms.EmailField()
         