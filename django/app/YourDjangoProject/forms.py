from django import forms


class DebugForm(forms.Form):
    def say_hello(self):
        return "Hello From Debug Form!"
