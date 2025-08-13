from .models import Registration, Team
from hackathons.models import Hackathon
from django.conf import settings

def auto_match_teams(hackathon_id):
    hackathon = Hackathon.objects.get(id=hackathon_id)
    registrations = Registration.objects.filter(hackathon=hackathon, status='registered')
    max_size = hackathon.max_team_size

    # Sort registrations by preferred role (optional)
    sorted_regs = sorted(registrations, key=lambda r: r.preferred_role)

    teams = []
    current_team = []

    for reg in sorted_regs:
        current_team.append(reg.user)
        if len(current_team) == max_size:
            team = Team.objects.create(
                hackathon=hackathon,
                name=f"Team {len(teams)+1}"
            )
            team.members.set(current_team)
            teams.append(team)
            current_team = []

    # Handle leftover members
    if current_team:
        team = Team.objects.create(
            hackathon=hackathon,
            name=f"Team {len(teams)+1}"
        )
        team.members.set(current_team)
        teams.append(team)

    return teams
