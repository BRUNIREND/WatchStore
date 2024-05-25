from .models import Products
from django.forms import ModelForm, TextInput,IntegerField, URLField, CharField, ChoiceField


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"
    class Meta:
        model = Products
        fields = {'name', 'cost', 'slug', 'discount', 'quantity', 'image',  'url_path', 'url_img', 'article', 'gender', 'country', 'waterproof', 'type_mechanism', 'category'}

        widgets = {
            'name': TextInput(attrs={'class': 'form-input'}),

        }