from django import forms
from .models import Staff

class StaffInsertForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('Full_name','Designation','Expertise','Phone_num','Email','Profile_Picture','Date_of_Birth')