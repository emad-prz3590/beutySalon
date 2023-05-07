from django import forms

class ArticleSearchForm(forms.Form):
    query = forms.CharField(label='جستجوی مقالات', max_length=100)