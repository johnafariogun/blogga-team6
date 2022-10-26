from django.forms import ModelForm
from django import forms
from post.models import Post, Comment, Profile, Category
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextField



class PostForm(forms.ModelForm):
    # # contents = SummernoteTextField()
    # # model = Post
    contents = forms.CharField(widget=SummernoteWidget())

    
    class Meta:
        model = Post
        fields = ['title', 'status', 'description','category','image','tags','contents']
        widgets = {
        "title": forms.Textarea(
        attrs={'style':'resize:none;','class': 'meta','placeholder':'Enter your title here'}
        ),
    
        'tags': forms.Textarea(
            attrs={ 'style':'resize:none;','class': 'meta','placeholder':'Enter your tags here'}
        ),
        # # category= forms.ModelChoiceField(queryset=Category.objects.all() )
        # # # status = forms.CharField(widget=forms.Select(choices=Post.choices))

        "description": forms.Textarea(
            attrs={'style':'resize:none;','class': 'meta','placeholder':'Enter your post description here'}
        ),
# <input type="file" name="image" accept="image/*" id="id_image">
        # "image": forms.ImageField(
            # attrs={''}
        # )
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email','comment')
        # widgets = {
        #     'comment': forms.Textarea(
        #         attrs={'placeholder':"Add a comment.." ,'style':"resize: none;", 'rows':"4", 'cols':"50", "name":"comment", 'form':"usrform" }
        #     )
        # }


class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ('avatar',)

class ContactForm(forms.Form):
    """this is a form for users to cntact us on what they need from our site"""
    first_name = forms.CharField(max_length = 300,required = True,label='First Name',
         widget= forms.TextInput(
            attrs={'class': '', 'id' :'contact_fname','placeholder':'FIRST NAME'}
    )) 
    last_name = forms.CharField(max_length = 300,required = True,label='Last Name', widget= forms.TextInput(
        attrs={'class': '', 'contact_lname' :'','placeholder':'LAST NAME'}
    )) 
    email = forms.EmailField(required = True,label='Email', widget= forms.EmailInput(
        attrs={'class': '', 'id' :'contact_email','placeholder':'email@email.com'}
    )) 
    message_ = forms.CharField(max_length = 5000,required = True,label='First Name', widget= forms.Textarea(
        attrs={'rows':10, 'cols':30,'class': '', 'id' :'contact_message','placeholder':'Your Message'}
    )) 

