from django import forms
from django.forms import Textarea
from .models import Comments, Articles, ProductsBorsch
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class CreateArticleForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото для шапки статьи',
        required=False,
        widget=forms.FileInput(attrs={'class': ''})
    )

    title = forms.CharField(
        label='Название статьи',
        required=True,
        widget=forms.TextInput(attrs={'class': 'registration_form_field', 'placeholder': 'Название статьи'}),
    )

    text = forms.CharField(
        label='Название статьи',
        required=True,
        widget=SummernoteWidget(attrs={'class': 'create_article_text_field', 'placeholder': 'Название статьи'}),
    )


    class Meta:
        model = Articles
        text = SummernoteTextField()
        fields = [
            'title',
            'text',
            'img',
        ]
        # widgets = {
        #     'text': SummernoteWidget(),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# SAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETY
# SAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETY
# SAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETYSAFETY

class UpdateArticleForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото для шапки статьи',
        required=False,
        widget=forms.FileInput(attrs={'class': ''})
    )

    title = forms.CharField(
        label='Название статьи',
        required=True,
        widget=forms.TextInput(attrs={'class': 'registration_form_field', 'placeholder': 'Название статьи'}),
    )

    text = forms.CharField(
        label='Название статьи',
        required=True,
        widget=SummernoteWidget(attrs={'class': 'create_article_text_field', 'placeholder': 'Название статьи'}),
    )

    class Meta:
        model = Articles
        text = SummernoteTextField()
        fields = [
            'title',
            'img',
            'text',
        ]
        # widgets = {
        #     'text': SummernoteWidget(),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = (
            'text',
        )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields['text'].widget = Textarea(attrs={'class': 'comment_form_text_field', 'placeholder': 'Ваш комментарий', 'rows': 5,})


class BorschForm(forms.ModelForm):
    name = forms.CharField(
        label='Наименование продукта',
        required=True,
        widget=forms.TextInput(attrs={'class': 'registration_form_field', 'placeholder': 'Наименование продукта'}),
    )

    price = forms.IntegerField(
        label='Стоимость продукта',
        required=True,
        widget=forms.TextInput(attrs={'class': 'registration_form_field', 'placeholder': 'Стоимость продукта'}),
    )

    grammovka = forms.IntegerField(
        label='Граммовка для литра борща',
        required=True,
        widget=forms.TextInput(attrs={'class': 'registration_form_field', 'placeholder': 'Граммовка для литра борща'}),
    )


    class Meta:
        model = ProductsBorsch
        fields = (
            'name',
            'price',
            'grammovka',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UpdateBorschForm(forms.ModelForm):
    name = forms.CharField(
        label='Наименование продукта',
        required=True,
        widget=forms.TextInput(attrs={'class': 'registration_form_field', 'placeholder': 'Наименование продукта'}),
    )

    price = forms.IntegerField(
        label='Стоимость продукта',
        required=True,
        widget=forms.TextInput(attrs={'class': 'registration_form_field', 'placeholder': 'Стоимость продукта'}),
    )

    grammovka = forms.IntegerField(
        label='Граммовка для литра борща',
        required=True,
        widget=forms.TextInput(attrs={'class': 'registration_form_field', 'placeholder': 'Граммовка для литра борща'}),
    )

    class Meta:
        model = ProductsBorsch
        fields = [
            'name',
            'price',
            'grammovka',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)