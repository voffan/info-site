from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import NON_FIELD_ERRORS
from info.models import Order


class AddOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'name',
            'email',
            'phone',
            'description'
        ]
        error_messages = {
            'name': {'required': 'Вы забыли ввести ваше имя!'},
            'email': {'required': 'Вы забыли ввести электронную почту!', 'invalid': 'Проверьте адрес электронной почты!'},
            'phone': {'required': 'Вы забыли ввести номер телефона!'},
            'description': {'required': 'Вы забыли ввести описание задачи!'},
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите свое имя'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите свой email'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер своего телефона'}),
            'description': Textarea(attrs={'class': 'form-control', 'style': 'width:100%;', 'rows':4}),
        }