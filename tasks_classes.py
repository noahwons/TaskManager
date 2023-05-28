# Import Libraries

import csv
import sys
import datetime
import random
from termcolor import colored, cprint
from dates_functions import *
from dates_functions import date_scheduled

# Global Variables

FILE = "csv_files/tasks.csv"

# User Defined Classes

class Task():
    def __init__(self, description=None, category=None, priority_level=None):
        if description:
            self.description = description
        if category:
            self.category = category
        if priority_level:
            self.priority_level = priority_level
        else:
            self.description = input("What is the description of the task? ")
            self.category = input("What is the category of the task? ").lower().strip()
            self.priority_level = input("What is the priority level of the task (1-5)? ")

        self.categories = ["school", "chore", "work"]
        self.id = 0

    def __str__(self):
        return f"Save status: {self.description}\nCategory: {self.category}\nPriority Level: {self.priority_level}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):  # Find more elagant solution to no previous id in "tasks.csv"
        try:
            with open(FILE) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    previd = row["id"]
            self._id = int(previd) + 1
        except UnboundLocalError:
            self._id = id + 1

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, categories):
        self._categories = categories

    @property
    def description(self):
        """Returns the description of the task"""
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of the task"""
        self._description = description

    @property
    def category(self):
        """Returns the category of the task"""
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of the task"""
        while True:
            if category in ["school", "chore", "work"]:
                self._category = category
                break
            else:
                print("Please enter a category related to one of the following: school, chore, work")
                category = input("What is the category of the task? ")

    @property
    def priority_level(self):
        """Returns the property level of the task"""
        return self._priority_level

    @priority_level.setter
    def priority_level(self, priority_level):
        """Sets the priority level of the task"""
        while True:
            try:
                if int(priority_level) > 5 or int(priority_level) < 1:
                    priority_level = input("What is the priority level of the task (1-5)? ")
                else:
                    break
            except ValueError:
                    priority_level = input("What is the priority level of the task (1-5)? ")
        self._priority_level = priority_level

    def save(self):
        """Save the user's task into 'tasks.csv'"""
        task = {"description": self.description, "category": self.category, "priority_level": self.priority_level, "id": self.id}
        with open(FILE, "a") as file:
            writer = csv.DictWriter(file, fieldnames=["description", "category", "priority_level", "id"])
            writer.writerow(task)
        save_text = colored(f"\n\nSucessfully saved task with id# {self.id}\n\n", "green")
        print(save_text)
        self.id += 1

