from django import forms
from .models import Category, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(
        max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

class DeleteForm(forms.Form):
    CATEGORY_CHOICES = []

    CATEGORY_CHOICES.append(('-1', 'Select'))
    for choice in Category.objects.all().order_by('category_name'):
        CATEGORY_CHOICES.append((choice.category_id, choice.category_name))

    # def __init__(self, *args, **kwargs):
    #     super(self.__class__, self).__init__(*args, **kwargs)
    #     global CATEGORY_CHOICES
    #     # CATEGORY_CHOICES = ['Select']
    #     # CATEGORY_CHOICES.append(('-1', 'Select'))
    #     for choice in Category.objects.all().order_by('category_name'):
    #         CATEGORY_CHOICES.append((choice.category_id, choice.category_name))
    #     # self.fields['category_id'].choices = CATEGORY_CHOICES
    pdf_file = forms.FileField(widget=forms.FileInput(attrs={'accept' : '.pdf'}))

    valves = forms.ModelChoiceField(required=False, widget=forms.Select, queryset=Category.objects.all().order_by('category_name'))
    # category_id = forms.CharField(label='category', widget=forms.Select(choices=CATEGORY_CHOICES
    # ,attrs={ 'class' : 'form-control',  "placeholder" : "Category", "style" : "height:35px" }
    # ))
    


class EditForm(forms.Form):
    CATEGORY_CHOICES = []

    CHOICES= (
    ('Home', 'Home'),
    ('Courses', 'Courses'),
    ('Login', 'Login'),
    ('Signup', 'Signup'),
    ('About US', 'About US'),
    ('Contact US', 'Contact US'),
    ('Dashboard', 'Dashboard'),
    ('Profile', 'Profile'),
    )
    CATEGORY_CHOICES.append(('-1', 'Select'))
    for choice in Category.objects.all().order_by('category_name'):
        CATEGORY_CHOICES.append((choice.category_id, choice.category_name))

    # def __init__(self, *args, **kwargs):
    #     super(self.__class__, self).__init__(*args, **kwargs)
    #     global CATEGORY_CHOICES
    #     # CATEGORY_CHOICES = ['Select']
    #     # CATEGORY_CHOICES.append(('-1', 'Select'))
    #     for choice in Category.objects.all().order_by('category_name'):
    #         CATEGORY_CHOICES.append((choice.category_id, choice.category_name))
    #     # self.fields['category_id'].choices = CATEGORY_CHOICES
    pdf_file = forms.FileField(widget=forms.FileInput(attrs={'accept' : '.pdf'}))

    valves = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    # valves = forms.ModelChoiceField(required=False, widget=forms.Select, queryset="Select")
    # category_id = forms.CharField(label='category', widget=forms.Select(choices=CATEGORY_CHOICES
    # ,attrs={ 'class' : 'form-control',  "placeholder" : "Category", "style" : "height:35px" }
    # ))


class ImportForm(forms.Form):
    CATEGORY_CHOICES = []

    CATEGORY_CHOICES.append(('-1', 'Select'))
    for choice in Category.objects.all().order_by('category_name'):
        CATEGORY_CHOICES.append((choice.category_id, choice.category_name))

    # def __init__(self, *args, **kwargs):
    #     super(self.__class__, self).__init__(*args, **kwargs)
    #     global CATEGORY_CHOICES
    #     # CATEGORY_CHOICES = ['Select']
    #     # CATEGORY_CHOICES.append(('-1', 'Select'))
    #     for choice in Category.objects.all().order_by('category_name'):
    #         CATEGORY_CHOICES.append((choice.category_id, choice.category_name))
    #     # self.fields['category_id'].choices = CATEGORY_CHOICES
    pdf_file = forms.FileField(widget=forms.FileInput(attrs={'accept' : '.pdf'}))

    valves = forms.ModelChoiceField(required=True, widget=forms.Select, queryset=Category.objects.all().order_by('category_name'))
    # category_id = forms.CharField(label='category', widget=forms.Select(choices=CATEGORY_CHOICES
    # ,attrs={ 'class' : 'form-control',  "placeholder" : "Category", "style" : "height:35px" }
    # ))
    

class ProfileForm(forms.ModelForm):

    phone = forms.CharField(max_length=300, required=True)
    bachelor_degree = forms.CharField(max_length=50, required=False, help_text='please enter bachelor degree')
    bachelor_yop = forms.CharField(max_length=254, help_text='please enter year of pass')
    master_degree = forms.CharField(max_length=50, required=False, help_text='Please enter master degree')
    master_yop = forms.CharField(max_length=300, required=False, help_text='please enter year of pass')
    specialization = forms.CharField(max_length=500, required=False, help_text='Please enter specalization')
    project_title = forms.CharField(max_length=500, required=False, help_text='Please enter project title')
    duration = forms.CharField(max_length=500, required=False, help_text='Please enter duration')
    tech_stack = forms.CharField(max_length=500, required=False, help_text='Please enter tech stack')
    project_description = forms.CharField(max_length=500, required=False, help_text='Please enter project description')
    first_name = forms.CharField(max_length=50, required=False, help_text='Please enter name')
    last_name = forms.CharField(max_length=50, required=False, help_text='Please enter name ')
    email = forms.CharField(max_length=50, required=False, help_text='Please enter email ')
    auth_user_id = forms.CharField(widget = forms.HiddenInput(), required = False)

    
    class Meta:
        model = Profile
        fields = [
            'phone',
            'bachelor_degree', 
            'bachelor_yop', 
            'master_degree',
            'master_yop',
            'specialization',
            'project_title',
            'duration',
            'tech_stack',
            'project_description',
            'auth_user_id',
            'first_name',
            'last_name',
            'email'
            ]
