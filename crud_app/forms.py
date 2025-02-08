from django.forms import ModelForm
from .models import Brand
from .models import ProductPresentation
from .models import Product

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields =  '__all__'
        
class ProductPresentationForm(ModelForm):
    class Meta:
        model = ProductPresentation
        fields =  '__all__'
