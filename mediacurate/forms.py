from django import forms
from form_utils.forms import BetterForm
from tagging_autocomplete.widgets import TagAutocomplete
from mediacurate.widgets import LocationAutocomplete
from mediacurate.models import Media

class AddForm(BetterForm):
    '''Used on the add page. Includes first review.'''
    url = forms.URLField()
    title = forms.CharField(help_text="If the current title is confusing or not descriptive, please edit it.")
    location = forms.CharField(widget=LocationAutocomplete)
    author_name = forms.CharField(widget=forms.widgets.TextInput(attrs={'readonly':True}))
    #author_url = forms.CharField(widget=forms.widgets.HiddenInput())
    author_url = forms.CharField(widget=forms.widgets.TextInput(attrs={'readonly':True}))
    
    name = forms.CharField(required=False,help_text="Tell us who you are.")
    review = forms.CharField(widget=forms.widgets.Textarea(),required=False,help_text="The more information you provide, the more useful it is to others. What made you want to add this to the collection? Is there a particularly good portion that viewers should watch out for?")
    tags = forms.CharField(widget=TagAutocomplete,required=True,help_text="Use existing tags before creating new ones.")
    
    date_uploaded = forms.CharField(widget=forms.widgets.TextInput(attrs={'readonly':True}),required=False)
    resolution = forms.CharField(widget=forms.widgets.TextInput(attrs={'readonly':True}),required=False)
    views = forms.IntegerField(widget=forms.widgets.TextInput(attrs={'readonly':True}),required=False)
    license = forms.CharField(widget=forms.widgets.TextInput(attrs={'readonly':True}),required=False)
    class Meta:
        fieldsets = (
            ('URL',{'fields':('url',),
                    'description':'Paste the URL to preview',
                    'classes':['']}
            ),
            ('Basic Information <b>(Required)</b>',{'fields':('title','location','tags',),
                    'description':"Where was this taken, and what is it about?",
                    'classes':['']}
            ),
            ('Data <b>(Not Editable)</b>',{'fields':('author_name','author_url','resolution','views','license','date_uploaded'),
                    'description':"This is information we pull from the host site.",
                    'classes':['hidden']}
            ),
            ('Review <b>(Optional)</b>',{'fields':('name','review'),
                    'description':"Please enter a review. It helps others to know what to look for, and helps us categorize the content.",
                    'classes':['review']}
            ),
        )