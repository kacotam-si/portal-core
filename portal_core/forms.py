from django import forms
from django.forms.utils import flatatt
from django.utils.html import format_html

from .validators import validate_non_strict_email


class NonStrictEmailField(forms.EmailField):
    default_validators = [validate_non_strict_email]


class ReadOnlyTextWidget(forms.Widget):
    def render(self, name, value, attrs):
        final_attrs = self.build_attrs(attrs)
        return format_html('<div{}>{}</div>', flatatt(final_attrs), value)


class ReadOnlyTextField(forms.Field):
    widget = ReadOnlyTextWidget

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('required', False)
        super(ReadOnlyTextField, self).__init__(*args, **kwargs)

    def bound_data(self, data, initial):
        return initial

    def has_changed(self, initial, data):
        return False
