from django.db import models
from django.conf import settings

class Registration(models.Model):
    ROLE_CHOICES = [
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('manager', 'Manager'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('registered', 'Registered'),
        ('shortlisted', 'Shortlisted'),
        ('matched', 'Matched'),
        ('withdrawn', 'Withdrawn'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='registrations'
    )
    hackathon = models.ForeignKey(
        'hackathons.Hackathon',  # ✅ updated to match your folder structure
        on_delete=models.CASCADE,
        related_name='registrations'
    )
    preferred_role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    skills = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='registered')

    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'hackathon')

    def __str__(self):
        return f"{self.user.email} → {self.hackathon.title} ({self.status})"
class Team(models.Model):
    hackathon = models.ForeignKey(
        'hackathons.Hackathon',
        on_delete=models.CASCADE,
        related_name='teams'
    )
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='teams'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.hackathon.title})"

    def member_count(self):
        return self.members.count()
