# task_schedule_python

import os
import datetime


FILE_NAME = "tasks.txt"


def validate_time(time_str):
    if time_str.endswith(("AM", "PM")) and len(time_str) in (3, 4):
        try:
            hour = int(time_str[:-2])
            if 1 <= hour <= 12:
                return True
        except ValueError:
            pass
    return False


tasks = []
if not os.path.exists(FILE_NAME):
    print("File does not exist. Starting with an empty task list.")
else:
    with open(FILE_NAME, "r") as file:
        for line in file:
            time, task = line.strip().split(" : ", 1)
            tasks.append((time, task))

while True:
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        if not tasks:
            print("No tasks available.")
        else:
            print("Current To-Do List:")
            for i, (time, task) in enumerate(tasks, 1):
                print(f"{i}. {time} : {task}")

    elif choice == "2":
        task_name = input("Enter task name: ").strip()
        while True:
            time = input("Enter time (12AM to 12PM): ").strip().upper()
            if validate_time(time):
                break
            else:
                print("Invalid time. Please enter a valid time between 12AM to 12PM.")
        tasks.append((time, task_name))
        tasks.sort(key=lambda x: (x[0][-2:], int(x[0][:-2]) % 12))
        with open(FILE_NAME, "w") as file:
            for time, task in tasks:
                file.write(f"{time} : {task}\n")
        print("Task added successfully.")

    elif choice == "3":
        if not tasks:
            print("No tasks available to delete.")
        else:
            print("Current To-Do List:")
            for i, (time, task) in enumerate(tasks, 1):
                print(f"{i}. {time} : {task}")
            while True:
                try:

                    choice = int(
                        input("Enter the number of the task to delete: "))
                    if 1 <= choice <= len(tasks):
                        removed_task = tasks.pop(choice - 1)
                        with open(FILE_NAME, "w") as file:
                            for time, task in tasks:
                                file.write(f"{time} : {task}\n")
                        print(
                            f"Task '{removed_task[1]}' deleted successfully.")
                        break
                    else:
                        print(
                            f"Please choose a number between 1 and {len(tasks)}.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
