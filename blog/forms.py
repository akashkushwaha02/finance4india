from django import forms    
from .models import Blog,BlogCategory

choices = BlogCategory.objects.all().values_list('name','name')

choices_list = []

for item in choices:
    choices_list.append(item)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','title_tag','category','author','description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list,attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','id':'author_name','value':'','type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),

        }

class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields =('title','title_tag','category','description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }