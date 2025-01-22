from django.db import models
from django.conf import settings
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField

# Managers
class PublishManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status='Recipe.Status.PUBLISHED')
        )

class FlaggedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(admin_status='Recipe.Admin_Status.FLAGGED')
        )

class AdminFlaggedManager(models.Manager):
    def get_queryset(self):
        return(
            super().get_queryset().filter(admin_status='Recipe.Admin_Status.ADMIN_FLAGGED')
        )


class Recipe(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PU', 'Published'

    class Admin_Status(models.TextChoices):
        NONE = 'NO', 'None'
        FLAGGED = 'FG', 'Flagged'
        ADMIN_FLAGGED = 'AFG', 'Admin Flagged'

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique_for_date='publish')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipes')
    description = models.TextField()
    article_1 = models.TextField()
    article_1_title = models.CharField(max_length=255, default='')
    article_2 = models.TextField(null=True, blank=True)
    article_2_title = models.CharField(max_length=255, default='')
    status = models.CharField(max_length=10, choices=Status, default=Status.DRAFT)
    admin_status = models.CharField(max_length=10, choices=Admin_Status, default=Admin_Status.NONE)
    main_image = models.ImageField(upload_to='images/', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    published = PublishManager()
    flagged = FlaggedManager()
    admin_flagged = AdminFlaggedManager()

    class Meta:
        ordering = ['-publish', 'title']
        indexes = [
            models.Index(fields=['-publish', 'title']),
        ]

    def __str__(self):
        return self.title

class Recipe_Images(models.Model):
    class Admin_Status(models.TextChoices):
        NONE = 'NO', 'None'
        FLAGGED = 'FG', 'Flagged'
        ADMIN_FLAGGED = 'AFG', 'Admin Flagged'

    title = models.CharField(max_length=255)
    description = models.TextField()
    Image = models.ImageField(upload_to='images/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='images')
    admin_status = models.CharField(max_length=10, choices=Admin_Status, default=Admin_Status.NONE)
    objects = models.Manager()
    admin_flagged = AdminFlaggedManager()

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created', 'title']),
        ]

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    class Admin_Status(models.TextChoices):
        NONE = 'NO', 'None'
        FLAGGED = 'FG', 'Flagged'
        ADMIN_FLAGGED = 'AFG', 'Admin Flagged'

    name = models.CharField(max_length=255)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    amount_unit = models.CharField(max_length=25, default='amount needed')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    date_added = models.DateTimeField(auto_now_add=True)
    group_name = models.CharField(max_length=255, default='main')
    group_number = models.IntegerField(default=1)
    admin_status = models.CharField(max_length=10, choices=Admin_Status, default=Admin_Status.NONE)
    objects = models.Manager()
    admin_flagged = AdminFlaggedManager()

    class Meta:
        ordering = ['group_number', 'name','-date_added']
        indexes = [
            models.Index(fields=['group_number','name','-date_added']),
        ]

    def __str__(self):
        return self.name


class Directions(models.Model):
    class Admin_Status(models.TextChoices):
        NONE = 'NO', 'None'
        FLAGGED = 'FG', 'Flagged'
        ADMIN_FLAGGED = 'AFG', 'Admin Flagged'

    title = models.CharField(max_length=255)
    number = models.IntegerField()
    description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='directions')
    date_added = models.DateTimeField(auto_now_add=True)
    admin_status = models.CharField(max_length=10, choices=Admin_Status, default=Admin_Status.NONE)
    group_name = models.CharField(max_length=255, default='main')
    group_number = models.IntegerField(default=1)
    objects = models.Manager()
    admin_flagged = AdminFlaggedManager()

    class Meta:
        ordering = ['-number']
        indexes = [
            models.Index(fields=['-number']),
        ]

    def __str__(self):
        return self.title