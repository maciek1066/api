from django import forms
from .models import Stock


class StockAddForm(forms.Form):
    class Meta:
        model = Stock
        fields = "__all__"

