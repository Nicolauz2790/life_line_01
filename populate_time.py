from database.manager import DatabaseManager
from models.time_tracking import TimeTracker
from datetime import datetime, timedelta
import random

def populate_time_data():
    db = DatabaseManager()
    tracker = TimeTracker(db)
    
    print("Populating Time Logs...")
    
    activities = [
        ("Coding", "Work"),
        ("Meeting", "Work"),
        ("Gym", "Health"),
        ("Running", "Fitness"),
        ("Cooking", "Chores"),
        ("Reading", "Leisure"),
        ("Sleeping", "Sleep"),
        ("Gaming", "Leisure"),
        ("Socializing", "Social")
    ]
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 07:00 - 08:00 Gym
    tracker.add_log("Morning Gym", "Health", today, "07:00", "08:00", 60, "Leg day")
    
    # 09:00 - 12:00 Work
    tracker.add_log("Deep Work", "Work", today, "09:00", "12:00", 180, "Focused coding")
    
    # 13:00 - 14:00 Lunch/Social
    tracker.add_log("Team Lunch", "Social", today, "13:00", "14:00", 60, "")
    
    # 14:00 - 17:00 Work
    tracker.add_log("Meetings", "Work", today, "14:00", "17:00", 180, "")
    
    # 19:00 - 21:00 Leisure
    tracker.add_log("Reading", "Leisure", today, "19:00", "21:00", 120, "Sci-Fi novel")

    print("Added 5 sample logs for today.")

if __name__ == "__main__":
    populate_time_data()
