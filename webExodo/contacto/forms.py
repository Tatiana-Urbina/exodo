from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Nombre'}
    ))
    mail = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Email'}
    ))
    mensaje = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'placeholder':'Dejanos tu consulta'}
    ))