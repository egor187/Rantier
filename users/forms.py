from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]