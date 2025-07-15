import json
import os
from datetime import datetime,timedelta

DATA_FILE = "habits.json"


#Load the habit data from file or returnempty dictionary is file doesnt exist
def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    else:
        return {}
    

# Save today's date as completed
def mark_today_done():
    habits = load_habits()
    today=datetime.now().strftime("%Y-%m-%d")
    habits[today]=True

    with open(DATA_FILE,"w") as f:
        json.dump(habits,f,indent=2)

    print(f"📅 Marked {today} as done.")

def get_streak(habits):

    streak =0
    today=datetime.now().date()

    #go backwards day by day
    for i in range(0,365):
        check_date= today - timedelta(days=i)
        key = check_date.strftime("%Y-%m-%d")

        if habits.get(key):
            streak+=1
        else:
            break
    return streak

