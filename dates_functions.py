# ==============================================================================================
# This module of the taskmanager program contains the code that handles the "dates.csv" file
# TODO: Remove a date of a task when it is deleted, maybe do this in the other file?
# ==============================================================================================
# Imported Files:

from tasks_classes import *
from tasks_functions import *


# ==============================================================================================
# Global Variables:
FILE = "csv_files/dates.csv"
dates_list = []
# Append Field-names
from datetime import date
with open(FILE, "r") as file:
    reader = csv.DictReader(file)
    dates_list.append(reader.fieldnames)

# ==============================================================================================
# User Defined Functions:


def is_empty():
    """Determines if the file is empty or not"""
    update_dates_list()
    if len(dates_list) == 1:
        text = colored(f"There are no tasks scheduled.","red")
        print(text)
        return True
    else:
        return False


def display_tasks():
    """Displays all tasks and scheduled dates (if any)"""
    update_tasks_list()
    if len(tasks_list) != 1:
        for i in range(len(tasks_list)):
            if i == len(tasks_list):
                break
            if i > 0:
                description = tasks_list[i]["description"]
                category = tasks_list[i]["category"]
                priority_level = tasks_list[i]["priority_level"]
                id_num = tasks_list[i]["id"]
                text = colored(f"{description}, Category: {category}, Priority Level: {priority_level}", "green")
                id_text = colored(f"{id_num}", "green")
                due_date = date_scheduled(tasks_list[i])  # due_date is the date that the task is scheduled for
                if due_date:  # If a value for due_date exists
                    due_date_text = colored(f"{due_date}", "green")
                    print(f"Task {i}: " + f"{text} with id#: {id_text}" + f", Scheduled, for: {due_date_text}")
                else:
                    print(f"Task {i}: " + f"{text} with id#: {id_text}")
    else:
        text = colored(f"There are no tasks in the file.","red")
        print(text)


def date_scheduled(task):
    """Returns the date that a task is scheduled for"""
    update_dates_list()
    for i in range(len(dates_list)):
        if i > 0:
            if dates_list[i]["id"] == task["id"]:
                return dates_list[i]["date"]
    return None


def delete_date(id):
    """Deletes a date from the file if the related task id completed"""
    # Update the list
    update_dates_list()
    dates_ids = []
    # Gather the ids in the list
    for index in range(len(dates_list)):
        if index != 0:
            dates_ids.append(dates_list[index]["id"])
    # Check if the "id" parameter is in the list
    if id in dates_ids:
        for date_index in dates_list:
            if date_index != dates_list[0]:  # If the index is not fieldnames
                if id == date_index["id"]:
                    id_date = date_index["date"]
                    index = dates_list.index({"id": id, "date": id_date})
                    del dates_list[index]
                    with open(FILE, "w+") as file:  # Re-write file
                        writer = csv.writer(file)
                        writer.writerow(dates_list[0])  # Re-write heading to csv file
                        my_file = csv.DictWriter(file, fieldnames=["id", "date"])
                        for i in range(len(dates_list)):
                            if i > 0:
                                my_file.writerow(dates_list[i])  # Re-write each date to the file with updated information


def update_dates_list():
    """Updates the dates_list to contain current information from the file if it is not already stored"""
    with open(FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row not in dates_list:
                dates_list.append(row)


def schedule(id):
    """Schedule the task with the given id to the user-specified date"""
    id_in_file_choice = check_id_in_file(FILE, id)
    if id_in_file_choice != 0 and id_in_file_choice != 1:  # Only schedule the task if it has not already been scheduled or rescheduled
        date = input("When should this task be completed?\nEx Format: YYYY-MM-DD\n\nDate: ")
        date = verify_iso(date)
        with open("csv_files/tasks.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["id"] == id:
                    edit(FILE, date, id)
        print(colored(f"Sucessfully scheduled task with id#{id} for '{date}'", "green"))


def verify_iso(x):
    """Verifys iso_format of 'x'"""
    while True:
        try:
            date.fromisoformat(x)
            break
        except ValueError:
            print(colored("\nInvalid format or date\n","red"))
            x = input("When should this task be completed?\nEx Format: YYYY-MM-DD\n\nDate: ")
    return x


def schedule_task():
    """Schedule a task for a user specified date"""
    if len(tasks_list) == 1:  # len of 1 means "tasks_list" only contains fieldnames
        print(colored("There are no tasks in the file to be scheduled", "red"))
    else:
        scheduled_task_id = input("Please enter the ID# of the task: ")
        scheduled_task_id = date_id_validation(scheduled_task_id)
        schedule(scheduled_task_id)


def edit(file, date, id):
    """Edits the contents of file"""
    with open(file, "a") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "date"])
        writer.writerow({"id": id, "date": date})


def date_id_validation(date_id):
    tasks_ids = []  # The only valid id's should be the id's of currently existing tasks
    for task in tasks_list:
        if task != tasks_list[0]:
            tasks_ids.append(task["id"])
    while date_id not in tasks_ids:
        print("invalid id")
        date_id = input("Please enter the ID# of the task: ")
    return date_id


def reschedule(file, id):
    """Changes the date that a tash should be completed by"""
    new_date = input("Please enter the new date (YYYY-MM-DD): ")
    new_date = verify_iso(new_date)
    if date_id_validation(id):
        rescheduled_date_id = id
        for date in dates_list:
            if date != dates_list[0]:  # If the "date" is not equal to fieldnames
                if date["id"] == rescheduled_date_id:
                    rescheduled_date_index = dates_list.index(date)  # Gets the index of the dictionary in the list
                    dates_list[rescheduled_date_index]["date"] = new_date  # Changes the date to the new date
        with open(file, "w+") as filew:  # Re-write file with completed task removed
            writer = csv.writer(filew)
            writer.writerow(dates_list[0])  # Re-write heading to csv file
            my_file = csv.DictWriter(filew, fieldnames=["id", "date"])
            for i in range(len(dates_list)):
                if i > 0:
                    my_file.writerow(dates_list[i])  # Re-write each date to the file with updated information
        text = colored(f"The task has been rescheduled for {new_date}","green")
        print(text)


def check_id_in_file(file, id):
    """Finds the row with the id, calls reschedule"""
    update_dates_list()
    for i in range(len(dates_list)):
        if i != 0:
            if dates_list[i]["id"] == id:
                date_at_index_i = dates_list[i]["date"]
                id_text = colored(f"{id}", "green")
                date_text = colored(f"{date_at_index_i}", "green")
                reschedule_input = input(f"Task with id# {id_text} is already scheduled for {date_text}, would you like to reschedule" + colored(" (y/n)? ","green"))
                # Check if input is valid
                while True:
                    if reschedule_input == "y" or reschedule_input == "n":
                        break  # Break loop if input is valid
                    else:
                        # Reprompt
                         reschedule_input = input(f"Task with id# {id_text} is already scheduled for {date_text}, would you like to reschedule" + colored(" (y/n)? ","green"))
                if reschedule_input == "y":
                    reschedule(file, id)
                    return 1  # A return value of 1 indicated that the date is found and has been rescheduled
                elif reschedule_input == "n":
                    return 0  # A return value of 0 indicated that the date is found and has not been rescheduled
    return 2  # The entire list must be checked before a value of 2 can be returned to confirm that the date has not already been scheduled


def reccomend():
    """Provide a reccomendation to the user"""
    iso_dates = []
    occurrences = 0  # if the amount of tasks due on the same day increases, the amount of occurences increases
    occurrence_ids = []
    occurrence_days = []
    todays_date = date.today()

    if not is_empty():  # If the file is not empty
        for date_date in dates_list:  # "date_date" is a place holder for each date in "dates_list" because "date" is used in the datetime library
            if date_date != dates_list[0]:
                iso_dates.append({"id": date_date["id"], "days": (date.fromisoformat(date_date["date"]) - todays_date).days})  # the id is the id of the task and the "days" is the difference between the due date of the task and when it should be accomplished
        lowest_value = min(i["days"] for i in iso_dates)  # This loop will itterate through the list and find the lowest value

        for i in range(len(iso_dates)):
            if lowest_value == iso_dates[i]["days"]:
                occurrences += 1
                occurrence_ids.append(iso_dates[i]["id"])
                occurrence_days.append(iso_dates[i]["days"])

        for i in range(len(occurrence_days)):
            if occurrence_days[i] < 0:
                negative_due_date_id = occurrence_ids[i]
                colored_negative_due_date_id = colored(f"{negative_due_date_id}", "red")
                choice = input(f"Task with id# {colored_negative_due_date_id} has a due-date that has" + colored(" expired", "red") + ".\nWould you like to reschedule" + colored(" (y/n)? ","green"))
                if choice == "y":
                    reschedule(FILE, occurrence_ids[i])

        if occurrences > 1 and occurrence_days[0] == 0: # If the task is due today and there are multiple occurrences
            occurrence_ids_str = ', '.join(id for id in occurrence_ids)  # the "join" method connects each element in the list
            occurrence_ids_str = colored(f"{occurrence_ids_str}", "green")
            days_colored = colored(f"{occurrence_days[0]}", "red")
            colored_advice = colored("Advice: Be sure to split youre time wisley! Take needed breaks and devote the proper amount of time to each task.", "green")
            print(f"Tasks with ids: {occurrence_ids_str} are due Today!, it is reccomended to work on both as soon as possible!\n{colored_advice}")

        if occurrences > 1 and occurrence_days[0] > 0:  # If the task is due after today and there are multiple occurrences
            occurrence_ids_str = ', '.join(id for id in occurrence_ids)  # the "join" method connects each element in the list
            occurrence_ids_str = colored(f"{occurrence_ids_str}", "green")
            days_colored = colored(f"{occurrence_days[0]}", "red")
            print(f"Tasks with ids: {occurrence_ids_str} are due in {days_colored} day(s), it is reccomended to work on both as soon as possible!\n" +
                colored("Advice: Be sure to split youre time wisley! Take needed breaks and devote the proper amount of time to each task.", "green"))

        if occurrences == 1 and occurrence_days[0] == 0:  # If the task is due today and there is only 1 occurrence
            colored_occurrence_ids = colored(f"{occurrence_ids[0]}" ,"green")
            print(f"It is reccomended to work on task with id# {colored_occurrence_ids}, beacuse it has the closest due-date of" + colored(" Today!", "red"))

        if occurrences == 1 and occurrence_days[0] > 0: # If the task is due after today and there is only 1 occurrence
            colored_occurrence_ids = colored(f"{occurrence_ids[0]}" ,"green")
            colored_occurrence_days = colored(f"{occurrence_days[0]}", "red")
            print(f"It is reccomended to work on task with id# {colored_occurrence_ids}, beacuse it has the closest due-date of {colored_occurrence_days} day(s)")


# ==============================================================================================
