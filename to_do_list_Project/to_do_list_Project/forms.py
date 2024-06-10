from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from to_do_list_App.models import *



class to_do_list_form(UserCreationForm):

    class Meta:
        model=custom_user
        fields= UserCreationForm.Meta.fields+('city','profile_picture','user_type','email','first_name','last_name')

class to_do_list_auth_form(AuthenticationForm):
    
    class Meta:
        model=custom_user
        fields=('username','password')
