from oscar.apps.dashboard.catalogue import forms as base_forms
from oscar.apps.dashboard.catalogue.forms import ProductForm as CoreProductForm

class ProductForm(base_forms.ProductForm):
    class Meta(base_forms.ProductForm.Meta):
        fields = CoreProductForm.Meta.fields + [
            'title',
            'upc',
            'description',
            'is_public',
            'is_discountable',
            'structure',
            'slug',
            'meta_title',
            'meta_description',
            'start_date',
            'end_date',
            'is_approved',
        ]
