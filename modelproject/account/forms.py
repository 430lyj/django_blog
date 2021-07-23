from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import fields
from .models import CustomUser

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={ 'class': 'signup-inputs',
                                        'placeholder': '아이디를 입력하세요'})
        )
    password1 = forms.CharField(
        label="",
        help_text="문자, 숫자, 기호를 조합하여 8자 이상을 사용하세요",
        widget=forms.PasswordInput(attrs={'class': 'signup-inputs',
                                          'placeholder': '비밀번호를 입력하세요'})
        )
    password2 = forms.CharField(
        label="",
        help_text="",
        widget=forms.PasswordInput(attrs={'class': 'signup-inputs',
                                          'placeholder': '비밀번호 확인'})
        )
    nickname = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'signup-inputs',
                                          'placeholder': '닉네임을 입력하세요'})
        )
    university = forms.CharField(
        label="",
        help_text="예 : 한국외국어대학교",
        widget=forms.TextInput(attrs={'class': 'signup-inputs',
                                          'placeholder': '재학 중인 대학교를 입력하세요'})
        )
    location = forms.CharField(
        label="",
        help_text="예 : 서울시 동대문구 이문로 107",
        widget=forms.TextInput(attrs={'class': 'signup-inputs',
                                          'placeholder': '주소를 입력하세요'})
        )
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nickname', 'university', 'location']
