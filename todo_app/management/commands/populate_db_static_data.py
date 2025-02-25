from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random
from faker import Faker

from todo_app.models import User, Tasks
from django.db import transaction


class Command(BaseCommand):
    help = 'Creates random data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        # get or create superuser
        # using context manager if it fails de population we don't trash the db.
        with transaction.atomic():
            user = User.objects.create_superuser(username='carlos', password='carlos')
            user1 = User.objects.create_user(username='pedro', password='roberto')
            user2 = User.objects.create_user(username='claudia', password='gonzales')
            user3 = User.objects.create_user(username='nicolino', password='roche')
            user4 = User.objects.create_user(username='ricardo', password='Fort')

            Tasks.objects.create(
                user=user,
                title="Clean the room",
                description="You need to clean the room",
                status=Tasks.StatusChoices.CREATED
            )
            Tasks.objects.create(
                user=user1,
                title="Visit Grandma",
                description="Go to her home",
                status=Tasks.StatusChoices.CREATED
            )
            Tasks.objects.create(
                user=user2,
                title="Study Go",
                description="Go Better than Rust ?",
                status=Tasks.StatusChoices.CREATED
            )
            Tasks.objects.create(
                user=user3,
                title="Eat Vegetables",
                description="They are good for you",
                status=Tasks.StatusChoices.CREATED
            )
            Tasks.objects.create(
                user=user4,
                title="Go outside",
                description="Get some vitamin D",
                status=Tasks.StatusChoices.CREATED
            )

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with STATIC data'))