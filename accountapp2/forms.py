from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # UserCreationForm과 다를게 없음 -> 하지만 *args, **kwargs를 이용해 커스터마이징 가능
        self.fields['username'].disabled = True