from pyexpat import model
from django import forms
from product.models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields ="__all__"

class UpdateForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields =     ['product_name','product_price','product_details','product_description']