from django import forms

from .models import Status


# For validation of input data in Status posts.
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    # form supports clean_<field_name> to specify validation of a field
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 240:
            raise forms.ValidationError('Content is too long')
        return content

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        if content == '':
            content = None

        image = data.get('image', None)
        if content is None and image is None:
            raise forms.ValidationError('Content or image is required.')

        return super().clean(*args, **kwargs)
