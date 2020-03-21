from utilities.filters import BaseFilterSet

from .models import ExampleModel


class ExampleFilterSet(BaseFilterSet):

    class Meta:
        model = ExampleModel
        fields = ['id', 'name']