from django.db import models
from accounts.models import User
from hackathons.models import Hackathon

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.hackathon.title}"
