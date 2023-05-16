# todo_list.py

import json
from json import JSONDecodeError
from datetime import datetime

date_format = "%d.%m.%Y %H:%M"
categories_file = "categories.json"
tasks_file = "tasks.json"


# Function to load categories from file
def load_categories():
    try:
        with open(categories_file, "r") as file:
            categories = json.load(file)
    except FileNotFoundError:
        categories = []
    except JSONDecodeError:
        categories = []

    return categories


# Function to save categories to file
def save_categories(categories):
    with open(categories_file, "w") as file:
        json.dump(categories, file)


# Function to add a new category
def add_category(category):
    categories = load_categories()

    if category in categories:
        print("The category already exists.")
    else:
        categories.append(category)
        save_categories(categories)
        print("The category has been added successfully.")


# Function to load tasks from file
def load_tasks():
    try:
        with open(tasks_file, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    except JSONDecodeError:
        tasks = []
    return tasks


# Function to save tasks to file
def save_tasks(tasks):
    with open(tasks_file, "w") as file:
        json.dump(tasks, file)


# Function to add a new task
def add_task():
    task_list = load_tasks()
    tasks_name = []
    for i in task_list:
        tasks_name.append(i['task'])
    print(tasks_name)
    categories = load_categories()
    print("categories: ",categories)
    task = input("Enter a task: ")
    if (task in tasks_name):
        print("The task already exists.")
    else:
        deadline = input("Enter the deadline (e.g., 22.01.2022 21:30): ")
        try:
            datetime.strptime(deadline, date_format)
        except ValueError:
            print("Input is not in the correct date format.")
        responsible = input("Enter the responsible person: ")
        category = input("Enter the category: ")
        if (category in categories):
            new_task = {
                "task": task,
                "deadline": deadline,
                "responsible": responsible,
                "category": category
            }
            task_list.append(new_task)
            save_tasks(task_list)
            print("The task has been added successfully.")
        else:
            print("The category does not exist.")
            


# Function to display tasks
def display_tasks(tasks):
    for task in tasks:
        print("Task:", task["task"])
        print("Deadline:", task["deadline"])
        print("Responsible:", task["responsible"])
        print("Category:", task["category"])
        print()


# Function to sort tasks
def sort_tasks(tasks, key):
    print(len(tasks))
    if len(tasks) != 0:
        tasks.sort(key=lambda x: x[key])
    return tasks


# Function to filter tasks
def filter_tasks(tasks, field, value):
    filtered_tasks = [task for task in tasks if task[field].startswith(value)]
    return filtered_tasks


# Function to edit a task
def edit_task(tasks):
    display_tasks(tasks)
    task_name = input("Enter the name of the task you want to edit: ")

    for item in tasks:
        if item["task"] == task_name:
            field = input("Enter the field you want to edit (task, deadline, responsible, category): ")
            if field not in ["task", "deadline", "responsible", "category"]:
                print("The entered field does not exist.")
            else:
                new_value = input("Enter the new value: ")
                print(tasks)
                item[field]=new_value
                
                #tasks.update({field:new_value})
            print("The task has been updated successfully.")
            save_tasks(tasks)
            


# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    task_name = input("Enter the name of the task you want to delete: ")
    for item in tasks:
        if item["task"] == task_name:   
            tasks.remove(item)
            print("task eliminat!")
            save_tasks(tasks)
        
    print("The task does't exists.")


def show_menu():
    while True:
        print("Menu:")
        print("1. List tasks")
        print("2. Sort tasks")
        print("3. Filter tasks")
        print("4. Add a new task")
        print("5. Edit a task")
        print("6. Delete a task")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            tasks = load_tasks()
            tasks = sort_tasks(tasks, "category")
            display_tasks(tasks)
        elif option == "2":
            sort_option = input("Enter the sort option (1-8): \n1.Sortare ascendenta task\n2.Sortare descendeta task\n3.Sortare ascendenta data\n4.Sortare descendeta data\n5.Sortare ascendenta persoana responsabila\n5.Sortare descendeta persoana responsabila\n6.Sortare ascendenta categorie\n8.Sortare descendeta categorie\n")
            tasks = load_tasks()

            if sort_option == "1":
                tasks = sort_tasks(tasks, "task")
            elif sort_option == "2": 
                tasks = sort_tasks(tasks, "task")
                tasks.reverse()
            elif sort_option == "3":
                tasks = sort_tasks(tasks, "deadline")
            elif sort_option == "4":
                tasks = sort_tasks(tasks, "deadline")
                tasks.reverse()
            elif sort_option == "5":
                tasks = sort_tasks(tasks, "responsible")
            elif sort_option == "6":
                tasks = sort_tasks(tasks, "responsible")
                tasks.reverse()
            elif sort_option == "7":
                tasks = sort_tasks(tasks, "category")
            elif sort_option == "8":
                tasks = sort_tasks(tasks, "category")
                tasks.reverse()
            else:
                print("Invalid sort option.")

            display_tasks(tasks)
        elif option == "3":
            filter_field = input("Enter the field for filtering (1-4): ")
            filter_value = input("Enter the filter value: ")
            tasks = load_tasks()

            if filter_field in ["1", "2", "3", "4"]:
                filtered_tasks = filter_tasks(tasks, {
                    "1": "task",
                    "2": "deadline",
                    "3": "responsible",
                    "4": "category"
                }[filter_field], filter_value)
                display_tasks(filtered_tasks)
            else:
                print("Invalid filter field.")
        elif option == "4":
            add_task()
        elif option == "5":
            tasks = load_tasks()
            edit_task(tasks)
        elif option == "6":
            tasks = load_tasks()
            delete_task(tasks)
        elif option != "0":
            print("Invalid option.")
        else:
            break


def main():
    while True:
        print("Enter the task categories (type 'exit' to finish):")
        category = input("Category: ")

        if category == "exit":
            break

        add_category(category)
        


main()
show_menu()

