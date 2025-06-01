# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Generate customized reminder
match priority:
    case "high" | "medium" | "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print(f"\nReminder: '{task}' has an unspecified priority. Please check and update the priority level.")
