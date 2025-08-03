from django import forms
from django.contrib.auth.models import User
from .models import Item,CATEGORY_CHOICES

class Registerform(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control p-2','placeholder': 'Enter your username','style':'margin-left:160px; width:500px;'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control p-2','placeholder': 'Enter your email','style':'margin-left:160px; width:500px;'})) 
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control p-2','placeholder': 'Enter your password','style':'margin-left:160px; width:500px;'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control p-2','placeholder': 'Confirm password','style':'margin-left:160px; width:500px;'}))
    class Meta: 
        model=User
        fields=['username',"email","password"]
        help_texts={
            'username':""
        }
    
    def clean_email(self):
        email=self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use")
        else:
            return email
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

class Loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control p-2','placeholder': 'Enter your username','style':'margin-left:160px; width:500px;'}))    
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control p-2','placeholder': 'Enter your Password','style':'margin-left:160px; width:500px;'}))

class ItemForm(forms.ModelForm):
    category=forms.ChoiceField(choices=CATEGORY_CHOICES,widget=forms.Select(attrs={'class': 'form-select p-2','placeholder': 'Choose Category','style':' width:500px;','id': 'category-select'}))
    name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control p-2','placeholder': 'Enter your name','style':' width:500px;' }))
    description=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control p-2','placeholder': 'Enter Description','style':' width:500px;' }))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control p-2','placeholder': 'Enter Price','style':' width:500px;' }))
    class Meta:
        model=Item
        fields=["category","name","description","price","image"]

