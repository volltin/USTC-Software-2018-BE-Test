from django import forms
from .models import UserMain
from django.utils.translation import ugettext_lazy as _


# -------------
# 用户登入表单
# author: roar
# -------------
class UserLoginForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].required = True
        self.fields['password'].required = True

    class Meta:
        model = UserMain

        fields = ['username', 'password']

        labels = {'username': _('Username'), 'password': _('Password')}

        widgets = {
            'username': forms.TextInput(
                attrs={
                    "placeholder": _("Username"),
                },
            ),

            'password': forms.PasswordInput(
                attrs={
                    "placeholder": _('Password'),
                },
            ),
        }

        error_messages = {
            'username': {
                'required': _('User name is required!')
            },

            'password': {
                'required': _('Password is required!')
            },
        }


# -------------
# 用户注册表单
# author: roar
# -------------
class UserRegisterForm(forms.Form):
    username = forms.CharField(
        required=True,

        label=_('Username'),

        error_messages={
            "required": _('please enter user name!'),
        },

        widget=forms.TextInput(
            attrs={
                "placeholder": _("Username"),
            }
        ),

    )

    password = forms.CharField(
        required=True,

        label=_('Password'),

        error_messages={
            "required": _("Please enter your password"),
        },

        widget=forms.PasswordInput(
            attrs={
                "placeholder": _("Password"),
            }
        ),

    )

    password_confirm = forms.CharField(
        required=True,

        label=_('Password confirmation'),

        error_messages={
            "required": _("Please enter your password confirmation"),
        },

        widget=forms.PasswordInput(
            attrs={
                "placeholder": _('Password confirmation'),
            }
        ),

    )

    email = forms.EmailField(
        required=True,
        label=_("Email"),
        error_messages={
            "required": _("Please enter your email address"),
        },
        widget=forms.EmailInput(
            attrs={
                "placeholder": _("Email address"),
            }
        ),
    )

