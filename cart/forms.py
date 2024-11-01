from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

class CartAddProductForm(forms.Form):
     quantity = forms.TypedChoiceField(
          choices=PRODUCT_QUANTITY_CHOICES,
          coerce=int,
          label="Количество",
          widget=forms.Select(attrs={
               'class': 'form-control',
               'style': 'position: relative; height: 35px; width: 45px; top: -30px; left: 110px;'
          })
     )
     override = forms.BooleanField(               
               required=False, 
               initial=False, 
               widget=forms.HiddenInput
     )