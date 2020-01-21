from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):

    use_in_migrattions = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('メールアドレスが必要です。')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_suoerUser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staf', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('スーパーユーザーはis_staff=Treuである必要があります。')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('スーパーユーザーはis_superuser=Treuである必要があります。')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'

    # ユーザー名から NULL制約、ユニーク制約、入力必須制限を除去
    username = models.CharField(
        _('username'),
        max_length=150,
        blank=False,
        null=False,
        help_text="半角アルファベット、半角数字、@/./+/-/_ で150文字以下にしてください。",
        validators=[AbstractUser.username_validator],
    )
    # メールアドレスを必須にしてユニーク制約を付与
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


# def update_login_count(sender, user, **kwargs):
#     """
#     A signal receiver which updates the last_login date for
#     the user logging in.
#     """
#     user.login_count += 1
#     user.save(update_fields=['login_count'])
#
#
# user_logged_in.connect(update_login_count)
