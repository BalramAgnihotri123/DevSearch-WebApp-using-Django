from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, skill

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name",'password1', 'password2'] 
        labels = {
            "first_name": "Name",
            "username": "UserName",
        }
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {"class" : "input", "placeholder" : "Add field"}
                )
            
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name", "username", "location", "short_intro", 'profile_image' , "bio", "github_link", "website_link", "twitter_link"
        ]
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {"class" : "input"}
                )
            
class SkillForm(ModelForm):
    class Meta:
        model = skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {"class" : "input"}
                ) 