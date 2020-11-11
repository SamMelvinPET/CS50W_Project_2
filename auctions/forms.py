from django import forms


from auctions.models import Listing


class NewListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title',
                  'description',
                  'starting_bid',
                  'imageurl',
                  'category'
                  ]
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows':5})
            }