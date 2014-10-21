# _*_coding=utf8 _*_
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=200, label=u'主题')
    email = forms.EmailField(label=u'邮箱')
    message = forms.CharField(widget=forms.Textarea, label=u'内容')
    
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 1:
            raise forms.ValidationError(u"多给我点信息，让我更好地回复您")
        return message