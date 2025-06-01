# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process and generate customized reminder
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unspecified priority level"

# Append time-sensitivity message
if time_bound == "yes":
    print(f"Reminder: {message} that requires immediate attention today!")
else:
    print(f"Note: {message}. Consider completing it when you have free time.")
