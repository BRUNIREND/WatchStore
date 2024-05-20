from .models import Products
from django.forms import ModelForm, TextInput,IntegerField, URLField, CharField, ChoiceField


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = {'name', 'cost', 'url_path', 'url_img', 'article', 'gender', 'country', 'waterproof', 'type_mechanism'}

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара'
            }),

            'article': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Артикль'
            }),
            'country': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страна'
            }),
            'waterproof': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Водостойкость'
            }),
            'type_mechanism': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип механизма'
            })
        }