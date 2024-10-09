from django import forms
from slugify import slugify
from goods.models import Categories, Product


class AddProductForm(forms.ModelForm):
    # name = forms.CharField(max_length=150, label='Наименование продукта', widget=forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 50%", 'placeholder': "Name of product"}))
    # slug = forms.SlugField(max_length=250, label='URL', required=False, widget=forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 50%", 'placeholder': "Slug"}))
    # description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "id": "floatingTextarea2", "style": "width: 50%; height: 150px", 'placeholder': "Products description"}), label='Описание товара', required=False)
    # price = forms.IntegerField(min_value=0, max_value=1000000, required=False, label='Цена в российских рублях', widget=forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 50%", 'placeholder': "Name of product"}))
    # quantity = forms.IntegerField(min_value=0, max_value=100000, required=False, label='Количество в шт.', widget=forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 50%", 'placeholder': "Number of product"}))
    # discount = forms.IntegerField(min_value=0, max_value=99, required=False, label='Скидка в %', widget=forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 50%", 'placeholder': "Discount"}))
    # is_published = forms.BooleanField(required=False, initial=True, label='Статус')
    # category = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Категория', empty_label='Категория не выбрана', widget=forms.Select(attrs={'class': "form-select", 'id': "floatingSelect", 'aria-label': "Floating label select example", 'rows': 10, 'cols': 5}))

    class Meta:
        model = Product
        fields = ['name', 'slug', 'description', 'price', 'quantity', 'discount', 'is_published', 'category']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 40%", 'placeholder': "Name of product"}),
            'slug': forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 40%", 'placeholder': "Slug"}),
            'description': forms.Textarea(attrs={"class": "form-control", "id": "floatingTextarea2", "style": "width: 40%; height: 150px", 'placeholder': "Products description"}),
            'price': forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 25%", 'placeholder': "Name of product"}),
            'quantity': forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 25%", 'placeholder': "Number of product"}),
            'discount': forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 15%", 'placeholder': "Discount"}),
            'is_published': forms.Select(attrs={'class': "form-select", 'id': "floatingSelect", 'aria-label': "Floating label select example", 'rows': 2, 'cols': 5}),
            'category': forms.Select(attrs={'class': "form-select", 'id': "floatingSelect", 'aria-label': "Floating label select example", 'rows': 10, 'cols': 5}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name:
            cleaned_data['slug'] = slugify(name, separator='-', lowercase=True)
        return cleaned_data
