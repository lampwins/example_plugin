from django.http import HttpResponse

from utilities.views import ObjectListView, ObjectEditView

from .models import ExampleModel
from . import filters, tables, forms


class ExampleListView(ObjectListView):
    queryset = ExampleModel.objects.all()
    filterset = filters.ExampleFilterSet
    filterset_form = forms.ExampleFilterForm
    table = tables.ExampleTable


def hello_world(request):
    return HttpResponse('Hello World!')