from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from datetime import date, timedelta

# Remove user if they haven't activated their account within 7 days
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = User.objects.filter(is_active=False)

        for user in users:
            start_date = user.date_joined.date()
            end_date = start_date + timedelta(days=7)

            if end_date < date.today():
                User.objects.get(pk=user.id).delete()