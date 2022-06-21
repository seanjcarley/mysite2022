from pyexpat import model
from django import forms
from .models import Volume

class GetTrafficData(forms.ModelForm):
    class Meta:
        model = Volume
        fields = (
            'start_date', 'end_date', 'interval', 'direction', 'vehicle_class',
        )

    def __init__(self, *args, **kwargs):
        ''' add placeholders, set/remove labels, set autofocus '''
        super().__init__(*args, **kwargs)

        placeholders = {
            'start_date':'', 
            'end_date': '', 
            'interval': '', 
            'direction': '', 
            'vehicle_class':'',
        }

        self.fields['start_date'].widget.attrs['autofocus'] = True
        