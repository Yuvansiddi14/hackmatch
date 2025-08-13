from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(
        self,
        email,
        first_name,
        last_name,
        srn,
        semester,
        branch,
        password=None,
        **extra_fields
    ):
        """
        Creates and saves a regular User with the given email and required fields.
        """
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            srn=srn,
            semester=semester,
            branch=branch,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        first_name,
        last_name,
        srn,
        semester,
        branch,
        password=None,
        **extra_fields
    ):
        """
        Creates and saves a SuperUser with is_staff and is_superuser flags.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            email,
            first_name,
            last_name,
            srn,
            semester,
            branch,
            password,
            **extra_fields
        )

class User(AbstractUser):
    srn = models.CharField(max_length=20, unique=True)
    semester = models.PositiveSmallIntegerField()
    branch = models.CharField(max_length=100)

    # Remove the username field and use email as the unique identifier
    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "srn", "semester", "branch"]

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.srn})"
