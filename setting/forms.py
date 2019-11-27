from django import forms

from .models import Post


# from .models import Post, Comment, Image

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

'''
class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()



    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # image 필드 삭제
        fields = ['content',]

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file',]

ImageFormSet = forms.inlineformset_factory(Post, Image, form=ImageForm, extra=3)

'''
