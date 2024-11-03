from django import forms
from slugify import slugify
from goods.models import Categories, Product
from django.utils.safestring import mark_safe
from string import Template

# class ImagePreviewWidget(forms.widgets.FileInput):
#     def render(self, name, value, attrs=None, **kwargs):
#         html = Template("""<img src="$link"/>""")
#         return mark_safe(html.substitute(link=value))
#


class AddProductForm(forms.ModelForm):
    # name = forms.CharField(max_length=150, label='Наименование продукта', widget=forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 50%", 'placeholder': "Name of product"}))
    # slug = forms.SlugField(max_length=250, label='URL', required=False, widget=forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 50%", 'placeholder': "Slug"}))
    # description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "id": "floatingTextarea2", "style": "width: 50%; height: 150px", 'placeholder': "Products description"}), label='Описание товара', required=False)
    # price = forms.IntegerField(min_value=0, max_value=1000000, required=False, label='Цена в российских рублях', widget=forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 50%", 'placeholder': "Name of product"}))
    # quantity = forms.IntegerField(min_value=0, max_value=100000, required=False, label='Количество в шт.', widget=forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 50%", 'placeholder': "Number of product"}))
    # discount = forms.IntegerField(min_value=0, max_value=99, required=False, label='Скидка в %', widget=forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 50%", 'placeholder': "Discount"}))
    # is_published = forms.BooleanField(required=False, initial=True, label='Статус')
    # category = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Категория', empty_label='Категория не выбрана', widget=forms.Select(attrs={'class': "form-select", 'id': "floatingSelect", 'aria-label': "Floating label select example", 'rows': 10, 'cols': 5}))
    # photo = forms.ImageField(widget=ImagePreviewWidget,)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"
        self.fields['image'].empty_label = "Файл не выбран"
        self.fields['image'].checkbox_name = "Файл"
        #self.fields['category'].level_indicator = "&nbsp;" # = "Категория не выбрана"
        #self.fields['category'].label_from_instance = lambda obj: f"{' ' * (obj.level * 4)}{obj.name}"

    class Meta:
        model = Product
        fields = ['name', 'slug', 'description', 'product_status', 'image', 'price', 'quantity', 'discount', 'is_published', 'category']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 40%", 'placeholder': "Name of product"}),
            'slug': forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 40%", 'placeholder': "Slug"}),
            'description': forms.Textarea(attrs={"class": "form-control", "id": "floatingTextarea2", "style": "width: 40%; height: 150px", 'placeholder': "Products description"}),
            'image': forms.ClearableFileInput(attrs={'class': "form-control", 'id': "formFile", 'style': 'width: 40%'}),
            'price': forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 10%", 'placeholder': "Name of product"}),
            'quantity': forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 10%", 'placeholder': "Number of product"}),
            'discount': forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "style": "width: 10%", 'placeholder': "Discount"}),
            'is_published': forms.Select(attrs={'class': "form-select", 'id': "floatingSelect", 'aria-label': "Floating label select example", 'rows': 2, 'cols': 5}),
            'category': forms.Select(attrs={'class': "form-select", 'id': "floatingSelect", 'aria-label': "Floating label select example", 'rows': 10, 'cols': 5}),
            'product_status': forms.Select(
                attrs={'class': "form-select", 'id': "floatingSelect", 'aria-label': "Floating label select example", "style": "width: 10%"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name:
            cleaned_data['slug'] = slugify(name, separator='-', lowercase=True)
        return cleaned_data
