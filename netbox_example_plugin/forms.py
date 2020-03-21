from django import forms

from utilities.forms import BootstrapMixin

from .models import ExampleModel


class ExampleForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = ExampleModel
        fields = (
            'name',
        )


class ExampleFilterForm(BootstrapMixin, forms.Form):
    model = ExampleModel
    q = forms.CharField(
        required=False,
        label='Search'
    )
