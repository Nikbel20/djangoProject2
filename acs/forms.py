from tkinter import Image

from django import forms

from acs.models import Img


class ImageForm(forms.ModelForm):
    class Meta:
        model = Img
        fields = ['Image', 'title']
