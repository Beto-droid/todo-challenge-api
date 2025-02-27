from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random
from faker import Faker

from todo_app.models import User, Tasks
from django.db import transaction


class Command(BaseCommand):
    help = 'Creates static data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        # using context manager if it fails de population we don't trash the db.
        with transaction.atomic():
            # user = User.objects.create_superuser(username='random', password='random')
            # user2 = User.objects.create_user(username='user2', password='user2')
            # user3 = User.objects.create_user(username='user3', password='user3')
            # user4 = User.objects.create_user(username='user4', password='user4')
            # user5 = User.objects.create_user(username='user5', password='user5')

            user1 = User.objects.get(username='pedro')
            user2 = User.objects.get(username='claudia')
            user3 = User.objects.get(username='nicolino')
            user4 = User.objects.get(username='ricardo')

            users_list = [user1, user2, user3, user4]

            # Create fake tasks
            for _ in range(30):
                Tasks.objects.create(
                    user=random.choice(users_list),
                    title=fake.sentence(),
                    description=fake.paragraph(),
                    status=Tasks.StatusChoices.CREATED
                )

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with RANDOM data'))