from django import forms

class ArticleSearchForm(forms.Form):
    search = forms.CharField(label='جستجوی مقالات', max_length=100)