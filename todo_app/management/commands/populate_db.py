from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random
from faker import Faker

from todo_app.models import User, Tasks
from django.db import transaction


class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        # get or create superuser
        # using context manager if it fails de population we don't trash the db.
        with transaction.atomic():
            user = User.objects.create_superuser(username='admin', password='admin')
            user1 = User.objects.create_user(username='user1', password='user1')
            user2 = User.objects.create_user(username='user2', password='user2')
            user3 = User.objects.create_user(username='user3', password='user3')
            user4 = User.objects.create_user(username='user4', password='user4')

            users_list = [user, user1, user2, user3, user4]

            # Create fake tasks
            for _ in range(10):
                Tasks.objects.create(
                    user=random.choice(users_list),
                    title=fake.sentence(),
                    description=fake.paragraph(),
                    status=Tasks.StatusChoices.CREATED
                )

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data'))