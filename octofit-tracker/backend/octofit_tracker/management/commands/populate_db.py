from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='john.doe@example.com', name='John Doe', age=25, gender='Male', team='Team A'),
            User(_id=ObjectId(), email='jane.smith@example.com', name='Jane Smith', age=30, gender='Female', team='Team B'),
            User(_id=ObjectId(), email='alice.jones@example.com', name='Alice Jones', age=28, gender='Female', team='Team A'),
            User(_id=ObjectId(), email='bob.brown@example.com', name='Bob Brown', age=35, gender='Male', team='Team B'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team_a = Team(_id=ObjectId(), name='Team A')
        team_a.save()
        team_a.members.set([users[0], users[2]])

        team_b = Team(_id=ObjectId(), name='Team B')
        team_b.save()
        team_b.members.set([users[1], users[3]])

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Running', duration=30, calories_burned=300, date=date(2025, 4, 1)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Cycling', duration=60, calories_burned=600, date=date(2025, 4, 2)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Swimming', duration=45, calories_burned=450, date=date(2025, 4, 3)),
            Activity(_id=ObjectId(), user=users[3], activity_type='Yoga', duration=30, calories_burned=200, date=date(2025, 4, 4)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=team_a, points=100),
            Leaderboard(_id=ObjectId(), team=team_b, points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Morning Run', description='A 5km run to start the day', duration=30, difficulty='Easy'),
            Workout(_id=ObjectId(), name='Cycling Session', description='An hour-long cycling session', duration=60, difficulty='Medium'),
            Workout(_id=ObjectId(), name='Swimming Laps', description='45 minutes of swimming laps', duration=45, difficulty='Hard'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
