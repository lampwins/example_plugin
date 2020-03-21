from utilities.tables import BaseTable, ToggleColumn

from .models import ExampleModel


class ExampleTable(BaseTable):
    pk = ToggleColumn()

    class Meta(BaseTable.Meta):
        model = ExampleModel
        fields = ('pk', 'name')
