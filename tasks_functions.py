# ==============================================================================================
# This module of the taskmanager program contains the code that handles the "tasks.csv" file
# ==============================================================================================
# Imported Files:

from tasks_classes import *


# ==============================================================================================
# Global Variables:

tasks_list = []  # Fieldnames are always located at tasks_list[0]
FILE = "csv_files/tasks.csv"
with open(FILE, "r") as file:
    reader = csv.DictReader(file)
    tasks_list.append(reader.fieldnames)

# ==============================================================================================
# User Defined Functions:


def update_tasks_list():
    """Updates the tasks_list to contain current information from the file if it is not already stored"""
    with open(FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row not in tasks_list:
                tasks_list.append(row)


def completed_task_validation(task_id):
    valid_ids = []
    for task in tasks_list:
        if task != tasks_list[0]:
            valid_ids.append(task["id"])
    while task_id not in valid_ids:
        print("invalid task")
        task_id = input("Please enter the ID# of the completed task: ")
    return task_id


def complete_task():
    """Remove a task from the 'tasks.csv' file"""
    congrats_list = ["Keep up the great work!", "You're doing fantastic!"]
    if len(tasks_list) != 1:  # Cheack if there is information in the file
        completed_task_id = input("Please enter the ID# of the completed task: ")
        completed_task_id = completed_task_validation(completed_task_id)
        if completed_task_id:
            for task in tasks_list:
                if task != tasks_list[0]:  # If the "task" is not equal to heading
                    if task["id"] == completed_task_id:
                        completed_task_index = tasks_list.index(task)  # Gets the index of the dictionary in the list
                        del tasks_list[completed_task_index]  # Deletes the completed task from the list
            # Re-write file with completed task removed
            with open(FILE, "w+") as file:
                writer = csv.writer(file)
                writer.writerow(tasks_list[0])  # Re-write heading to csv file
                my_file = csv.DictWriter(file, fieldnames=["description", "category", "priority_level", "id"])
                for i in range(len(tasks_list)):
                    if i > 0:
                        my_file.writerow(tasks_list[i])  # Re-write each task to the file with updated information
            text = colored(f"Congradulations on completing a task! {random.choice(congrats_list)}\nHere are the remaining tasks:\n","green")
            print(text)
            return completed_task_id




# ==============================================================================================
