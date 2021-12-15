from django import forms
from django.core.exceptions import ValidationError
from .models import Post
from .validators import validate_symbols
# class PostForm(forms.Form):
#     title = forms.CharField(max_length=50, label='제목')
#     content = forms.CharField(widget=forms.Textarea, label='내용')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content']
        widgets = {'title': forms.TextInput(attrs={
            'class': 'title',
            'placeholder': '제목을 입력하세요'}),
            'content': forms.Textarea(attrs={
            'placeholder': '내용을 입력하세요'})}

    def clean_title(self):
        title = self.cleaned_data['title']
        if "*" in title:
            raise ValidationError('"*"가 포함될 수 없습니다')

        return title