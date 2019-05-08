# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.staticfiles.templatetags.staticfiles import static
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    @staticmethod #create unique username
    def create_username(username_temp):
        turkish_characters = {"ı": "i",
                "ç": "c",
                "ş": "s",
                "ü": "u",
                "ö": "o",
                "ğ": "g"}
        username_temp = username_temp.lower()
        for character in turkish_characters:
            if character in username_temp:
                username_temp = username_temp.replace(character, turkish_characters[character])
        j = 1
        k = ''
        for i in CustomUser.objects.all():
            if i.username == username_temp + str(k):
                k = j
                j = j+1
        username = username_temp+str(k)
        return username

    def create_user(self, first_name, last_name, email, password, **extra_fields):
        """
        Create and save a user with the given first_name, last_name, email, and password.
        username = first_name + last_name + [number] 
        """

        if not first_name:
            raise ValueError('The given firstname must be set')
        if not last_name:
            raise ValueError('The given lastname must be set')

        email = self.normalize_email(email)
        first_name = self.model.normalize_username(first_name)
        last_name = self.model.normalize_username(last_name)

        username_temp = first_name+last_name
        username = self.create_username(username_temp)

        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email,
                          first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, first_name, last_name, password=None):
        u = self.create_user(first_name, last_name, email, password)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u

class CustomUser(AbstractUser):
    # add additional fields in here
    email = models.EmailField(
        _('email'),
        max_length=150,
        unique=True,
        
        error_messages={
            'unique': _("Bu e-posta  adresi ile bir hesap bulunuyor."),
        },
    )
    user_photo = models.ImageField(upload_to='user_profile_photos/', default='/male-icon-19.png')

    about = models.TextField(_('hakkında'),max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()
    

    def __str__(self):
        return self.email
