from django import forms
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput
from .models import BlogPost


class PostForm(forms.ModelForm):
    """
    Form for editing a blog post
    """
    class Meta:
        model = BlogPost
        widgets = {
            'body': SummernoteWidget()
        }
        fields = [
            'title',
            'slug',
            'body',
            'image',
        ]
    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)


class AddPostForm(forms.ModelForm):
    """
    Form for adding a blog post
    """
    class Meta:
        model = BlogPost
        widgets = {
            'body': SummernoteWidget()
        }

        fields = [
            'title',
            'slug',
            'body',
            'image',
        ]
    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'