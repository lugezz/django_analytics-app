from django.forms import ChoiceField, DateInput, DateField, Form

CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),
)

RESULT_CHOICES = (
    ('#1', 'transaction'),
    ('#2', 'sales date'),
)


class SalesSearchForm(Form):
    date_from = DateField(widget=DateInput(attrs={'type': 'date'}))
    date_to = DateField(widget=DateInput(attrs={'type': 'date'}))
    chart_type = ChoiceField(choices=CHART_CHOICES)
    results_by = ChoiceField(choices=RESULT_CHOICES)
