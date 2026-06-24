from django.db import models

class Resume(models.Model):

    TEMPLATE_CHOICES = [
        ('student', 'Student'),
        ('professional', 'Professional'),
        ('modern', 'Modern'),
        ('creative', 'Creative'),
        ('developer', 'Developer'),
        ('executive', 'Executive'),
    ]

    template = models.CharField(
        max_length=20,
        choices=TEMPLATE_CHOICES,
        default='student'
    )

    # Personal Information
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    address = models.CharField(
        max_length=200,
        blank=True
    )

    linkedin = models.URLField(
        blank=True
    )

    github = models.URLField(
        blank=True
    )

    portfolio = models.URLField(
        blank=True
    )

    # Optional Photo
    photo = models.ImageField(
        upload_to='photos/',
        blank=True,
        null=True
    )

    # Resume Sections
    summary = models.TextField()

    education = models.TextField()

    skills = models.TextField()

    experience = models.TextField(
        blank=True
    )

    projects = models.TextField(
        blank=True
    )

    certifications = models.TextField(
        blank=True
    )

    achievements = models.TextField(
        blank=True
    )

    languages = models.CharField(
        max_length=200,
        blank=True
    )

    hobbies = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return self.full_name