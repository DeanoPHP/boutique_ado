from django import forms
from .models import UserProfile
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, classes, autofocus and patch crispy-country field issue
        """
        super().__init__(*args, **kwargs)

        # Force evaluation of choices to avoid 'BlankChoiceIterator' crash
        self.fields["default_country"].choices = list(CountryField().choices)
        self.fields["default_country"].widget = CountrySelectWidget()

        placeholders = {
            "default_phone_number": "Phone Number",
            "default_postcode": "Postal Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County, State or Locality",
        }

        self.fields["default_phone_number"].widget.attrs["autofocus"] = True

        for field in self.fields:
            if field != "default_country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder

            self.fields[field].widget.attrs[
                "class"
            ] = "border-black rounded-0 profile-form-input"
            self.fields[field].label = False
