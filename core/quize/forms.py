from django import forms 
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib import messages

class UserForm(forms.ModelForm): # Form for user registration
    confirm_password = forms.CharField(widget=forms.PasswordInput) # Field to confirm password
    class Meta: # Meta class to specify model and fields
        model = User
        fields = [ 'first_name', 'last_name','username', 'email', 'password' , 'confirm_password']    
    
    def clean(self): # Custom validation to check if passwords match
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            self.add_error('confirm_password', "Password and Confirm Password do not match.")
        return cleaned_data
    def save(self, commit=True): # Override save method to hash password
        user = super().save(commit=False)  
        user.set_password(self.cleaned_data["password"])
        if commit:  
            user.save() 
        return user


