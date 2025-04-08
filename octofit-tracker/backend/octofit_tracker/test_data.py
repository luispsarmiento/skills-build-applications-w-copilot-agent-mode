from bson import ObjectId
from datetime import timedelta

test_users = [
    {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
    {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
]

test_teams = [
    {"_id": ObjectId(), "name": "Blue Team", "members": [test_users[0], test_users[1]]},
    {"_id": ObjectId(), "name": "Gold Team", "members": [test_users[2], test_users[3], test_users[4]]},
]

test_activities = [
    {"_id": ObjectId(), "user": test_users[0], "activity_type": "Cycling", "duration": timedelta(hours=1)},
    {"_id": ObjectId(), "user": test_users[1], "activity_type": "Crossfit", "duration": timedelta(hours=2)},
    {"_id": ObjectId(), "user": test_users[2], "activity_type": "Running", "duration": timedelta(hours=1, minutes=30)},
    {"_id": ObjectId(), "user": test_users[3], "activity_type": "Strength", "duration": timedelta(minutes=30)},
    {"_id": ObjectId(), "user": test_users[4], "activity_type": "Swimming", "duration": timedelta(hours=1, minutes=15)},
]

test_leaderboard = [
    {"_id": ObjectId(), "user": test_users[0], "score": 100},
    {"_id": ObjectId(), "user": test_users[1], "score": 90},
    {"_id": ObjectId(), "user": test_users[2], "score": 95},
    {"_id": ObjectId(), "user": test_users[3], "score": 85},
    {"_id": ObjectId(), "user": test_users[4], "score": 80},
]

test_workouts = [
    {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
    {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
    {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
    {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
    {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
]
