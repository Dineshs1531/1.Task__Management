from django import forms
from .models import User,Ourtask
from django.contrib.auth.forms import UserCreationForm


class UserdetailForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TaskdetailForm(forms.ModelForm):
    priority_choice = [
        ("Low",'Low'),
        ("Medium","Medium"),
        ("High","High"),
    ]
    # complete_choice = [
    #     ("1", "completed"),
    #     ("2", "Not completed"),
    # ]
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    due_date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    priority=forms.ChoiceField(choices=priority_choice,widget=forms.Select(attrs={'class':'form-select','type':'select'}))
    created_at = forms.DateField(required=False,widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    updated_at = forms.DateField(required=False,widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    Time = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control','type':'Time'}))
    completed_status = forms.TypedChoiceField(
        
        choices=((1, 'completed'), (0, 'Not Completed')),
        coerce=int,
        widget=forms.RadioSelect,
    )

    

    #

    class Meta:
        model=Ourtask
        exclude = []
        fields = ['title', 'description', 'due_date', 'created_at','updated_at','priority', 'Time', 'completed_status']
    
    
