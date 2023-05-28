# ==============================================================================================
# In this module of my final project my goal is to collect information about a task and store it
# Using CSV files and the sys library I will implement command-line functionality that works with exceptions
# Implemend datetime library functionality that supports planning dates
# IDEA: Possibly implement regex functionality that can determine the syntax of a new "task"
# Problems, faced:
# - Learning how to overwrite information in csv files
            # del tasks_list[int(completed_task_id)-1]  # The problem lies here, the code wants to remove the task at the completed_task_id instead of the actual index of the task in the "tasks_list", so when an id number is removed, ex 1, 2 ,3; if 2 is removed then the list of id's is 1,3 which does not make sense
            # print(tasks_list)  # Find how to fix line of code above, figure out how to find the index of a task with the "completed_task_id" instead of removing the date in "tasks_list" at the index of "completed_task_id"
            # Fixed: To solve this problem I went online to find how other people solved this problem. Turns out, it made the most sense to append all of the information into a list and then delete specified information then rewrite the file with the updated list
# Could not determine when the information in tasks_list should be updated
            # Fixed: I needed to change the update function to only add information if it is not already found in the list
# ==============================================================================================
# This module of the taskmanager program contains the main function and functions associated with properly running the program
# ==============================================================================================
# Imported Files:

from tasks_classes import *
from tasks_functions import *
from dates_functions import *

# ==============================================================================================
# Global Variables:

chore_kw = ["lawn", "laundry", "garbage", "clean"]
commands = {"new": "Create a new task", "complete": "Complete a task!", "schedule": "Schedule a task", "display tasks": "display all tasks", "reccomend": "recieve a reccomendation"}

# ==============================================================================================
# User Defined Functions:
# TODO: Move reccommend and schedule to seperate file that handles dates functions


def main():
    """The main function"""
    while True:
        update_dates_list()
        update_tasks_list()
        print_commands()



def generate_task():
    """Creates a task"""
    task = Task()
    return task


def print_commands():
    """Prints each command and the title of the program"""
    print(f"\nWelcome to TaskManager!\n\nThe available commands are: ")
    for command in commands:
        text = colored(f"--{command} : {commands[command]}--","green")
        print(text)
    command = input("\nEnter a command you would like to execute or press enter to exit the program: ").strip().lower()
    execute(command)

def execute(cmnd):
    """Execute the users command from the prompt"""
    validate_cmnd(cmnd)
    if cmnd == "new":
        generate_task().save()

    if cmnd == "schedule":
        schedule_task()

    if cmnd == "complete":
        id = complete_task()  # Gets the id of completed task and removes it
        delete_date(id)  # Removes a date if scheduled
        display_tasks()

    if cmnd == "display tasks":
        display_tasks()

    if cmnd == "reccomend":
        reccomend()


def validate_cmnd(cmnd):
    """Ensure command is in the list of commands"""
    if cmnd.strip().lower() == "":
        sys.exit(colored("Thank you for using TaskManager, Have a wonderful day! :)\n", "green"))
    elif cmnd.strip().lower() not in commands:
        text = colored(f"Please input a command from the list.","red")
        print(f"\n\n{text}\n\n")

# ==============================================================================================
# File Verification:

if __name__ == "__main__":
    main()
