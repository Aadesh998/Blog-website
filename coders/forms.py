from django import forms
from froala_editor.widgets import FroalaEditor
from coders.models import Postblog

class Postblogform(forms.ModelForm):
    class Meta:
        model = Postblog
        fields = ['Desc']